import pandas as pd
import matplotlib.pyplot as plt
import calendarific
import requests
import numpy as np
import argparse
import analysis
import clean
import os

def main():

    csv_name='plane_crash_data.csv'
    run = analysis.give_me_df(csv_name)
    crash = analysis.set_up(run)
    crash = clean.data_clean(crash)
    x='https://calendarific.com/api/v2'
    api_df = analysis.api_calendarific(x)
    analysis.plot_operator(crash)
    analysis.plot_location(crash)


if __name__ == "__main__":
    main()
