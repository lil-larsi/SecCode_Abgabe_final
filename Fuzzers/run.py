from guided_mutation_fuzzer_jpg.exp3_statement_coverage.exp3 import run_mutation_coverage_fuzzer_statement_coverage_jpg
from guided_mutation_fuzzer_bmp.exp3_statement_coverage.exp3 import run_mutation_coverage_fuzzer_statement_coverage_bmp
from mutation_fuzzer_jpg.exp1 import run_mutation_fuzzer_jpg
from mutation_fuzzer_bmp.exp1 import run_mutation_fuzzer_bmp
from guided_mutation_fuzzer_jpg.exp1_line_coverage.exp1 import run_mutation_coverage_fuzzer_line_coverage_jpg
from guided_mutation_fuzzer_jpg.exp2_branch_coverage.exp2 import run_mutation_coverage_fuzzer_branch_coverage_jpg
from guided_mutation_fuzzer_bmp.exp1_line_coverage.exp1 import run_mutation_coverage_fuzzer_line_coverage_bmp
from guided_mutation_fuzzer_bmp.exp2_branch_coverage.exp2 import run_mutation_coverage_fuzzer_branch_coverage_bmp


dir_path_git = "XX/Projektobjekt/Fuzzingffjpeg/src"                               
run_mutation_fuzzer_jpg(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/x/mutation_fuzzer_jpg/in")
run_mutation_fuzzer_bmp(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/mutation_fuzzer_bmp/in")
run_mutation_coverage_fuzzer_line_coverage_jpg(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/guided_mutation_fuzzer_jpg/exp1_line_coverage/in")
run_mutation_coverage_fuzzer_branch_coverage_jpg(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/guided_mutation_fuzzer_jpg/exp2_branch_coverage/in")
run_mutation_coverage_fuzzer_statement_coverage_jpg(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/guided_mutation_fuzzer_jpg/exp3_statement_coverage/in")
run_mutation_coverage_fuzzer_line_coverage_bmp(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/guided_mutation_fuzzer_bmp/exp1_line_coverage/in")
run_mutation_coverage_fuzzer_branch_coverage_bmp(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/guided_mutation_fuzzer_bmp/exp2_branch_coverage/in")
run_mutation_coverage_fuzzer_statement_coverage_bmp(run_time_in_min=30, dir_path_git=dir_path_git, seed_path="/home/lars/Fuzzer/Abgabe_SecCode/guided_mutation_fuzzer_bmp/exp3_statement_coverage/in")
