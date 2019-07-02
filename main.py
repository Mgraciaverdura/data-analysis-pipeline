import pandas as pd
import matplotlib.pyplot as plt
import calendarific
import requests
import numpy as np
import analysis

if __name__=="__main__":
    csv_name='plane_crash_data.csv'
    run = analysis.give_me_df(csv_name)
    crash = analysis.set_up(run)
    crash = analysis.date_clean(x)
    crash = analysis.data_clean(crash)
    analysis.plot_operator(crash)
    analysis.plot_location(crash)
    crash = analysis.api_calendarific(BASE_URL)