import subprocess
from fuzzingbook.Fuzzer import Runner
from fuzzing.fuzzing_coverage import call_gcov
import time

class ProgramRunner(Runner):
    def __init__(self, program, progMethod):
        """Initialize.  `program` is a program spec as passed to `subprocess.run()`"""
        self.program_path = program
        self.method = progMethod
        self.coverages = []
        self.branch_coverage = []
        self.line_coverage = []
        self.statement_coverage = []
        self.crashes = 0
        self.crash_timestamp = []
        self.time_stamp = []
        self.crashes_array = []
        self.outcomepass = 0
        self.outcomeunresolved = 0
        self.crashfile=[]
    def run_process(self, inp=""):
        """
        description: Run the program at specified programm_path with inputfile_path as `inp` as input with subprocess.run()

        input: 
        inp(str): path to the input file

        output:
        subprocess
        """
        exec_array = [self.program_path, self.method, inp]
        return subprocess.run(exec_array,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines=True)

    def run(self, inp=""):
        """
        description: Run the program at specified programm_path with inputfile_path as `inp` as input with subprocess.run() and evalute subprocess.run()

        input: 
        inp(str): path to the input file

        output:
        result: result of subprocess
        outcome: FAIL, PASS or UNRESOLVED
        """
        mutated_seed = inp[1]
        result = self.run_process(inp[0])

        if result.returncode == 0:
            outcome = self.PASS
            self.outcomepass = self.outcomepass + 1
        elif result.returncode < 0:
            outcome = self.FAIL
            self.crashes = self.crashes + 1
            self.crashfile.append(inp[1])
        else:
            outcome = self.UNRESOLVED
            self.outcomeunresolved = self.outcomeunresolved + 1

        self.coverages = call_gcov(self.program_path)
        self.line_coverage.append(self.coverages[0])
        self.branch_coverage.append(self.coverages[1])
        self.statement_coverage.append(self.coverages[2])
        self.crashes_array.append(self.crashes)
        self.time_stamp.append(time.time())
        return (result, outcome, mutated_seed)

    def return_line_coverage(self):
        return self.line_coverage

    def return_branch_coverage(self):
        return self.branch_coverage

    def return_call_coverage(self):
        return self.statement_coverage

    def return_crashes_array(self):
        return self.crashes_array

    def return_timestamp(self):
        return self.time_stamp

    def return_outcome_fail(self):
        return self.crashes

    def return_outcome_pass(self):
        return self.outcomepass

    def return_outcome_unresolved(self):
        return self.outcomeunresolved

    def return_crashfile(self):
        return self.crashfile


class ProgrammCoverageRunner(ProgramRunner):


    def return_actual_line_coverage(self):
        return self.line_coverage[-1]

    def return_actual_branch_coverage(self):
        return self.branch_coverage[-1]

    def return_actual_statment_coverage(self):
        return self.statement_coverage[-1]
