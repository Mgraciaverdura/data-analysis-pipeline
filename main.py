import pandas as pd
import matplotlib.pyplot as plt

import analysis

if __name__=="__main__":
    csv_name='plane_crash_data.csv'
    run = read(csv_name)
    crash = set_up(run)
    crash = data_cleaning(crash)
    crash = data_embellish(crash)
    plot_operator(crash)
    plot_location(crash)