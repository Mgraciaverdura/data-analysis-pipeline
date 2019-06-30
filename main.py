import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from analysis import *

if __name__=="__main__":

csv_crash='plane_crash_data.csv'

run = read(csv_crash)
crash = set_up(run)
crash = data_cleaning(crash)
crash = data_embellish(crash)
plot_operator(crash)
plot_location(crash)