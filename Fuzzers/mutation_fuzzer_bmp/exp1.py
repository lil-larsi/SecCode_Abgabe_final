
from fuzzing.fuzzer import MutationFuzzer
from fuzzing.fuzzing_runner import ProgramRunner
from fuzzing.compiler import delete_coverage_files
from fuzzing.compiler import fuzz_compile
from fuzzing.fuzzing_logger import Logger
import os
import time


def run_mutation_fuzzer_bmp(run_time_in_min, dir_path_git, seed_path):
    timeout = 60*run_time_in_min


    delete_coverage_files(dir_path=dir_path_git)
    exe_path = fuzz_compile(dir_path=dir_path_git, exec_name="mutation_fuzzer")
    runner_fuzzing = ProgramRunner(program=exe_path, progMethod="-e")
    mutation_fuzzer= MutationFuzzer(path_seeds=seed_path)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        result, outcome, mutated_seed = mutation_fuzzer.run(runner=runner_fuzzing)
    logger = Logger(fuzzer= mutation_fuzzer, runner = runner_fuzzing)
    logger.plot(path=os.path.abspath(os.path.join(seed_path, os.pardir)))
