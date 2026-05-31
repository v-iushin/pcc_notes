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
# 3. summary
#   results and errors log



# 1.
'''
from generate_data import *
generate_data()
'''



# 2.
from pathlib import Path

BASE = Path(__file__).parent
runs_dir = BASE/"runs"

run_files_e = []
valid_files_data = []

for run_file in runs_dir.iterdir():
    if not run_file.is_file():
        continue
    e_record = {
        "name": run_file.name,
        "IO_e": False,
        "ERR_e": False,
        "TRUNC_e": False,
        "EMPTY_e": False,
        "ZERO_e": False,
        "HEAD_e": False,
    }
    run_files_e.append(e_record)
    print(run_file.name)
    try:
        contents = run_file.read_text(encoding="utf-8")
    except (PermissionError, UnicodeDecodeError):
        print("IO ERROR")
        e_record["IO_e"] = True
        print()
        continue
    lines = contents.splitlines()
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
    
    any_error = any([
        e_record["IO_e"],
        e_record["ERR_e"],
        e_record["TRUNC_e"],
        e_record["EMPTY_e"],
        e_record["ZERO_e"],
        e_record["HEAD_e"],
    ])
    if any_error:
        continue
    data_record = {
        "name": run_file.name,
        "row_count": 0,
        "mean_angle": 0,
        "max_absolute_angle": 0,
    }
    valid_files_data.append(data_record)
    mean_angle = 0
    max_angle = 0
    for line in lines[data_start_index:]:
        words = line.split()
        angle = float(words[1])
        abs_angle = abs(angle)
        mean_angle += angle
        if abs_angle > max_angle:
            max_angle = abs_angle
    data_record["row_count"] = len(lines[data_start_index:])
    data_record["mean_angle"] = round(mean_angle / data_record["row_count"], 5)
    data_record["max_absolute_angle"] = max_angle



# 3
import json
import datetime

results = BASE/"results.json"
errors = BASE/"errors.log"

len_tot = len(run_files_e)
len_valid = len(valid_files_data)
len_fail = len(run_files_e) - len(valid_files_data)
timestamp = datetime.datetime.now().isoformat()
results_data = {
    "timestamp": timestamp,
    "summary": {
        "total": len_tot,
        "succeeded": len_valid,
        "failed": len_fail,
    },
    "files": valid_files_data,
}
results.write_text(json.dumps(results_data, indent=2))

errors.write_text("")
with errors.open("a") as er:
    for run_file_e in run_files_e:
        if any([
            run_file_e["IO_e"],
            run_file_e["ERR_e"],
            run_file_e["TRUNC_e"],
            run_file_e["EMPTY_e"],
            run_file_e["ZERO_e"],
            run_file_e["HEAD_e"],
        ]):
            er.write(f"Errors for {run_file_e['name']}: ")
            for key, value in run_file_e.items():
                if value is True:
                    er.write(f"{key} ")
            er.write("\n")
print()
