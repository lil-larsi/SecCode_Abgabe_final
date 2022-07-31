import random
import os
from fuzzingbook.Fuzzer import Fuzzer
from fuzzing.fuzzing_runner import ProgrammCoverageRunner
from fuzzing.utils_fuzzing import flip_random_character, insert_random_character, delete_random_character
from fuzzing.seed import Seeds
from fuzzing.grammar import nonterminals, ExpansionError


class MutationFuzzer(Fuzzer):
    def __init__(self, path_seeds, min_mutations=2, max_mutations=30):
        self.seeds = Seeds(path_seeds=path_seeds)
        self.path_mutated_seeds = os.path.join(os.path.abspath(os.path.join(path_seeds, os.pardir)), "in_mutated/")
        if not os.path.exists(self.path_mutated_seeds):
            os.mkdir(self.path_mutated_seeds)
        self.seed = self.seeds.content
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.mutaded_name = []
        for name in self.seeds.names:
            file_name = os.path.basename(name)
            self.mutaded_name.append(os.path.join(self.path_mutated_seeds, file_name))
        self.reset()

    def reset(self):
        self.population = self.seed
        self.seed_index = 0


    def mutate(self, s):
        """Return s with a random mutation applied"""
        mutators = [
            delete_random_character,
            insert_random_character,
            flip_random_character
        ]
        mutator = random.choice(mutators)
        return mutator(s)

    def create_candidate(self):
        candidate = random.choice(self.population)
        index = self.population.index(candidate)
        trials = random.randint(self.min_mutations, self.max_mutations)
        for i in range(trials):
            candidate = self.mutate(candidate)
        return index, candidate

    def fuzz(self):
        self.seed_index, self.mutated_seed = self.create_candidate()
        self.save_mutated_seed(in_mutaded_input_dir=True)
        return self.mutaded_name[self.seed_index], self.mutated_seed

    def save_mutated_seed(self, in_mutaded_input_dir: bool):
        if in_mutaded_input_dir:
            with open(self.mutaded_name[self.seed_index], 'wb') as f:
                f.write(self.mutated_seed)
        else:
            base_name = os.path.basename(self.mutaded_name[self.seed_index])
            path = os.path.join(self.seeds.path, base_name)
            with open(path, 'wb') as f:
                f.write(self.mutated_seed)

class MutationFuzzer_coverage(MutationFuzzer):
    def __init__(self, path_seeds, min_mutations=2, max_mutations=10):
        super().__init__(path_seeds, min_mutations, max_mutations)
        self.actual_coverage = 0
        self.coverages_seen = [0]
    
    def reset(self):
        super().reset()

        # Now empty; we fill this with seed in the first fuzz runs

    def run_line_coverage(self, runner):
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome, mutated_seed = super().run(runner)
        self.actual_coverage = ProgrammCoverageRunner.return_actual_line_coverage(runner)
        self.append_seed_if_better_coverage(outcome)
        return result, outcome, self.mutated_seed, self.actual_coverage

    def run_branch_coverage(self, runner):
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome, mutated_seed = super().run(runner)
        self.actual_coverage = ProgrammCoverageRunner.return_actual_branch_coverage(runner)
        self.append_seed_if_better_coverage(outcome)
        return result, outcome, self.mutated_seed, self.actual_coverage

    def run_statement_coverage(self, runner):
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome, mutated_seed = super().run(runner)
        self.actual_coverage = ProgrammCoverageRunner.return_actual_statment_coverage(runner)
        self.append_seed_if_better_coverage(outcome)
        return result, outcome, self.mutated_seed, self.actual_coverage

    def fuzz(self):
        mutaded_name, mutated_seed  = super().fuzz()
        return mutaded_name, mutated_seed


    def append_seed_if_better_coverage(self, outcome):
        if (outcome == ProgrammCoverageRunner.PASS) and self.actual_coverage > max(self.coverages_seen):
            # We have new coverage
            actual_coverage_formated = "{:.2f}".format(self.actual_coverage)
            file_name_with_file_format = os.path.basename(self.mutaded_name[self.seed_index])
            file_format = file_name_with_file_format.split(".")[-1]
            if "_coverage" in file_name_with_file_format:
                file_name_with_file_format = file_name_with_file_format.split("_coverage_")[0]
            file_name = file_name_with_file_format.split(".")[0]
            name = file_name + "_coverage_" + actual_coverage_formated + "." + file_format
            self.mutaded_name.append(os.path.join(self.path_mutated_seeds, name))
            self.population.append(self.mutated_seed)
            self.coverages_seen.append(self.actual_coverage)
            self.seed_index = self.population.index(self.mutated_seed)
            self.save_mutated_seed(in_mutaded_input_dir=False)
            self.seeds.reset()
            self.reset()
        
class Grammar_Fuzzer(Fuzzer):
    def __init__(self, grammar, dir_path, start_sym, max_nonterminals: int = 10, max_expansion_trials: int = 50, log: bool = False):
        self.grammar = grammar
        self.log = log
        self.start_symbol = start_sym
        self.max_nonterminals = max_nonterminals
        self.max_expansion_trials = max_expansion_trials
        self.path_grammar_seed = os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)), "in_grammar/")
        if not os.path.exists(self.path_grammar_seed):
            os.mkdir(self.path_grammar_seed)
        self.grammar_name = os.path.join(self.path_grammar_seed, "grammar.abc")
        self.grammar_seed = ""

    def fuzz(self):
        term = self.start_symbol
        while len(nonterminals(term)) > 0:
            symbol_to_expand = random.choice(nonterminals(term))
            expansions = self.grammar[symbol_to_expand]
            expansion = random.choice(expansions)
            new_term = term.replace(symbol_to_expand, expansion, 1)

            if len(nonterminals(new_term)) < self.max_nonterminals:
                term = new_term
                if self.log:
                    print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
                expansion_trials = 0
            else:
                expansion_trials += 1
                if expansion_trials >= self.max_expansion_trials:
                    raise ExpansionError("Cannot expand " + repr(term))
        term = BMPHeader + term #not resolved to find a header
        self.grammar_seed =  term
        self.save_grammar_seed()
        return self.grammar_name, self.grammar_seed
    
    def save_grammar_seed(self):
        with open(self.grammar_name, 'w') as f:
            f.write(self.grammar_seed)
