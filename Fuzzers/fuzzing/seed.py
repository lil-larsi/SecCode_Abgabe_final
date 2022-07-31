import glob
import os
from fuzzing.grammar import simple_grammar_fuzzer, SIMPLE_ABC_GRAMMAR, START_SYMBOL

class Seeds():
    def __init__(self, path_seeds:str):
        """ init with Path to the /in dir, where all seeds are saved """
        self.path = path_seeds
        self.names = []
        self.content = []
        self.get_seeds()

    def reset(self):
        self.names = []
        self.content = []
        self.get_seeds()

    def return_seed_content(self):
        return self.content

    def return_seed_names(self):
        return self.names

    def get_seeds(self):
        search_path = os.path.join(self.path, "*")
        for file in glob.glob(search_path):
            self.names.append(file)
        for file in self.names:
            with open(file, 'rb') as f:
                    self.content.append(f.read())


    def return_seeds(self)->list:
        """ returns content to the specified dir """
        search_path = os.path.join(self.path, "*")
        for file in glob.glob(search_path):
            self.names.append(file)
        for file in self.names:
            with open(file, 'rb') as f:
                    self.content.append(f.read())
        return self.content

class Grammar_Seeds():
    def __init__(self, path_seeds:str, number_seeds):
        self.number_seeds = number_seeds
        self.path = path_seeds
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.names = []
        self.content = []
        self.generate_seeds()

    def generate_seeds(self):
        for i in range(self.number_seeds):
            actual_name = "gammar" + str(i) + ".abc"
            path_name = os.path.join(self.path , actual_name)
            self.names.append(actual_name)
            grammar_seed = simple_grammar_fuzzer(grammar= SIMPLE_ABC_GRAMMAR, start_symbol=START_SYMBOL)
            self.content.append(grammar_seed)
            with open(path_name, 'w') as f:
                f.write(grammar_seed)
        