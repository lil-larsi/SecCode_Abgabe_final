import subprocess
import os
import glob

def fuzz_compile(dir_path:str, exec_name:str)->str:
    """
    description: compiles all files in dir

    input: 
    dir_path(str): string to dir path
    exec_name(str): wanted name for executable

    output:
    exe_path(str): path to the eecutable file
    """
    saved_cwd = os.getcwd()
    shell_string_base = "gcc --coverage -g -O0 -c -o " 
    os.chdir(dir_path)
    o_file_string = ""
    for c_file in glob.glob("*.c"):
        o_file = c_file[:-2] + ".o"
        o_file_string += o_file + " "
        shell_string = shell_string_base + o_file + " " + c_file
        subprocess.call(shell_string, shell=True)
    shell_call_final = "gcc " + o_file_string + " --coverage -O0 -lm -o " + exec_name
    subprocess.call(shell_call_final, shell=True)
    exe_path = os.path.join(dir_path, exec_name)
    os.chdir(saved_cwd)
    return exe_path

def delete_coverage_files(dir_path:str):
    saved_cwd = os.getcwd()
    os.chdir(dir_path)
    for gcno_file in glob.glob("*.gcno"):
        os.remove(gcno_file)
    for gcda_file in glob.glob("*.gcda"):
        os.remove(gcda_file)
    for gcov_file in glob.glob("*.gcov"):
        os.remove(gcov_file)
    for o_file in glob.glob("*.o"):
        os.remove(o_file)
    os.chdir(saved_cwd)