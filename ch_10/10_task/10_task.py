# TASK

# FAULT-TOLERANT MEASUREMENT

# 1. data generator
#   creates RUNS directory with
#   damped pendulum experiment data,
#   some files will be malformed
# 
# 2. pipeline
#   read files from RUNS and validate them
# 
# 3. results
#   resume and errors log

'''
# 1.
from generate_data import *
generate_data()
'''


# 2.
#! truncated
#! emtpy
#! header
#! ERR
#! zero
from pathlib import Path
#import json

BASE = Path(__file__).parent
runs_dir = BASE/"runs"

run_file_e = []

for run_file in runs_dir.iterdir():
    if not run_file.is_file():
        continue
    contents = run_file.read_text()
    lines = contents.splitlines()
    print(run_file.name)
    e_record = {
        "name": run_file.name,
        "ERR_e": False,
        "TRUNC_e": False,
        "EMPTY_e": False,
        "ZERO_e": False,
        "HEAD_e": False,
    }
    run_file_e.append(e_record)
    try:
        lines[0]
    except IndexError:
        print("EMPY FILE")
        e_record["EMPTY_e"] = True
        print()
        continue
    if "omega" not in lines[0]:
        print("NO HEADER")
        e_record["HEAD_e"] = True
    if e_record["HEAD_e"]:
        data_start_index = 1
    else:
        data_start_index = 2
    if len(lines) <= data_start_index:
        print("ZERO DATA")
        e_record["ZERO_e"] = True
        print()
        continue
    for line in lines[data_start_index:]:
        words = line.split()
        try:
            words[1]
        except IndexError:
            e_record["TRUNC_e"] = True
        if "ERR" in line:
            e_record["ERR_e"] = True
    if e_record["TRUNC_e"]: 
        print("TRUNCATED")
    if e_record["ERR_e"]: 
        print("ERR DATA")
    print()




print()
