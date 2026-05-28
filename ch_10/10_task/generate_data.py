# DAMPED PENDULUM

import math

def damped_pendulum():
    OMEGA = 3
    GAMMA = 0.1
    theta_0 = math.pi / 3
    for t in range(50):
        theta = theta_0 * math.exp(-GAMMA * t/10) * math.cos(OMEGA * t/10)
        print(round(theta, 5))

damped_pendulum()



# DATA GENERATOR

from pathlib import Path

BASE = Path(__file__).parent
runs_dir = Path(BASE/"runs")
runs_dir.mkdir(exist_ok=True)

def generate_data(runs_dir):
    for i in range(10):
        run_file = Path(runs_dir/f"run_{i}.txt")
        run_file.write_text(f"{i}")
        
generate_data(runs_dir)
