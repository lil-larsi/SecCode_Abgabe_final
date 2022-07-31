from fuzzing.fuzzer import MutationFuzzer_coverage
from fuzzing.fuzzing_runner import ProgramRunner
from fuzzing.compiler import fuzz_compile, delete_coverage_files
from fuzzing.fuzzing_logger import Logger
import os
import time


def run_mutation_coverage_fuzzer_branch_coverage_bmp(run_time_in_min, dir_path_git, seed_path):
    timeout = 60*run_time_in_min
    delete_coverage_files(dir_path=dir_path_git)
    exe_path = fuzz_compile(dir_path=dir_path_git, exec_name="guided_branch_mutation_fuzzer")
    mutation_guided_fuzzer = MutationFuzzer_coverage(path_seeds=seed_path, min_mutations=1, max_mutations=3)
    runner_fuzzing = ProgramRunner(program=exe_path, progMethod="-e")
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        result, outcome, mutated_seed, coverage = mutation_guided_fuzzer.run_line_coverage(runner=runner_fuzzing)
    logger = Logger(fuzzer= mutation_guided_fuzzer, runner = runner_fuzzing)
    logger.plot(path=os.path.abspath(os.path.join(seed_path, os.pardir)))
