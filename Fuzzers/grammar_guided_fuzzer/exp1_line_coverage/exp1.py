from fuzzing.seed import Grammar_Seeds
from fuzzing.fuzzer import MutationFuzzer_coverage
from fuzzing.fuzzing_runner import ProgrammCoverageRunner
from fuzzing.compiler import fuzz_compile, delete_coverage_files
from fuzzing.fuzzing_logger import Logger
import os
import time


def run_grammar_guided_line_coverage_fuzzer(run_time_in_min, dir_path_git, seed_path):
    timeout = 60*run_time_in_min
    delete_coverage_files(dir_path=dir_path_git)
    Grammar_Seeds(path_seeds=seed_path, number_seeds=10)
    exe_path = fuzz_compile(dir_path=dir_path_git, exec_name="guided_line_grammar_mutation_fuzzer")
    mutation_based_fuzzer = MutationFuzzer_coverage(path_seeds=seed_path, min_mutations=1, max_mutations=3)
    runner_fuzzing_grammar = ProgrammCoverageRunner(program=exe_path)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        result, outcome, mutated_seed, coverage = mutation_based_fuzzer.run_line_coverage(runner=runner_fuzzing_grammar)
    logger = Logger(fuzzer= mutation_based_fuzzer, runner = runner_fuzzing_grammar)
    logger.plot(path=os.path.abspath(os.path.join(seed_path, os.pardir)))