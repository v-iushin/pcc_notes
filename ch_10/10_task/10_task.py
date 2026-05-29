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



from generate_data import *

generate_data()