import subprocess
import glob
import os 

def call_gcov(exe_path:str):
    saved_cwd = os.getcwd()
    os.chdir(os.path.dirname(exe_path))
    gcov_information=[]
    for file in glob.glob("*.c"):
        file_information = [file]
        subproc = subprocess.run(["gcov", "-b", file], stdout=subprocess.PIPE, text=True)
        file_information.extend(get_coverages(subproc.stdout))
        gcov_information.append(file_information)
    results = evalute_coverages(gcov_information)
    os.chdir(saved_cwd)
    return results


def get_coverages(gcov_string:str):
    lines_position = gcov_string.index('Lines executed:') + 15
    branches_postion = gcov_string.index('Branches executed:') + 18
    if 'No calls' in  gcov_string:
        calls_percentage = 0
        calls_total = 0
        calls_used = 0
    else:
        calls_postion = gcov_string.index('Calls executed:') + 15
        calls_string = gcov_string[calls_postion:calls_postion+15]
        while not calls_string[-1].isdigit():
            calls_string = calls_string[:-1]
        calls_percentage = float(calls_string[:calls_string.index('%')])
        calls_total = int(calls_string[(calls_string.index('of')+3):])
        calls_used = int(calls_percentage * calls_total / 100)
    lines_string = gcov_string[lines_position:lines_position+15]
    branches_string = gcov_string[branches_postion:branches_postion+15]
    

    while not lines_string[-1].isdigit():
        lines_string = lines_string[:-1]
    while not branches_string[-1].isdigit():
        branches_string = branches_string[:-1]

    lines_percentage = float(lines_string[:lines_string.index('%')])
    lines_total = int(lines_string[(lines_string.index('of')+3):])
    branches_percentage = float(branches_string[:branches_string.index('%')])
    branches_total = int(branches_string[(branches_string.index('of')+3):])
    lines_used = int(lines_percentage * lines_total / 100)
    branches_used = int(branches_percentage * branches_total / 100)
    result = [lines_percentage, lines_total, lines_used, branches_percentage, branches_total, branches_used, calls_percentage, calls_total, calls_used]
    return result

def evalute_coverages(file_information: list):
    length = len(file_information)
    lines_overall = 0
    lines_used = 0
    branches_overall = 0
    branches_used = 0
    calls_overall = 0
    calls_used = 0
    for id in range(length):
        lines_overall += file_information[id][2]
        lines_used += file_information[id][3]
        branches_overall += file_information[id][5]
        branches_used += file_information[id][6]
        calls_overall += file_information[id][8]
        calls_used += file_information[id][9]
    lines_used_percentage = lines_used / lines_overall * 100
    branches_used_percentage = branches_used / branches_overall * 100
    calls_used_percentage = calls_used / calls_overall * 100
    return [lines_used_percentage, branches_used_percentage, calls_used_percentage]

