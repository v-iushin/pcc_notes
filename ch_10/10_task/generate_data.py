# DAMPED PENDULUM
# DATA GENERATOR

from pathlib import Path
import math
import random as r

def generate_data():
    BASE = Path(__file__).parent
    runs_dir = Path(BASE/"runs")
    runs_dir.mkdir(exist_ok=True)
    for i in range(31):
        OMEGA = round(r.uniform(2.5, 3.5), 2)
        GAMMA = round(r.uniform(0.05, 0.15), 2)
        THETA_0 = round(r.uniform(0.5, 1), 2)
        run_file = Path(runs_dir/f"run_{i}.txt")
        run_file.write_text(f"omega = {OMEGA} \t gamma = {GAMMA} \t theta_0 = {THETA_0}\ntime \t angle\n")
        draw1 = r.choice([0, 0, 0, 0, 1])
        draw2 = 0
        if draw1 == 1:
            draw2 = r.randint(1, 5)
            if draw2 == 1:      # missing header
                run_file.write_text(f"time \t angle\n")
        with run_file.open("a") as rf:
            for t in range(101):
                t_step = t / 10
                theta = THETA_0 * math.exp(-GAMMA * t_step) * math.cos(OMEGA * t_step)
                theta = round(theta, 2)
                if draw2 == 2:      # empty file
                    run_file.write_text("")
                    break
                if draw2 == 3:    # zero data
                    continue
                if draw2 == 4:    # non-numeric data
                    draw3 = r.randint(1, 10)
                    draw4 = r.randint(1, 10)
                    if draw3 == 1:
                        t_step = "ERR"
                    if draw4 == 1:
                        theta = "ERR"
                elif draw2 == 5:    # truncated row
                    draw5 = r.randint(1, 10)
                    if draw5 == 1:
                        rf.write(f"{t_step}\n")
                        continue
                rf.write(f"{t_step} \t {theta}\n")
        
#generate_data("runs")
