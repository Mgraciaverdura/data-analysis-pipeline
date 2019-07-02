import pandas as pd
import matplotlib.pyplot as plt
import calendarific
import requests
import numpy as np
from analysis import analysis

if __name__=="__main__":
    csv_name='plane_crash_data.csv'
    run = analysis.give_me_df(csv_name)
    crash = analysis.set_up(run)
    crash = analysis.data_clean(crash)
    x='https://calendarific.com/api/v2'
    api_df = analysis.api_calendarific(x)
    file_CSV(crash)
    plot_operator(crash)
    plot_location(crash)
    