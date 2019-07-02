import pandas as pd
import matplotlib.pyplot as plt
import calendarific
import requests
import numpy as np
import argparse

def give_me_df(DataFrame):
       crash = pd.read_csv(DataFrame)
       return crash

def set_up(crash):
       colnames = ['location','operator','date']
       crash = pd.DataFrame(crash, columns=colnames)
       return crash

def arg_crash():
       parser = argparse.ArgumentParser()
       parser.add_argument('--name', required=True)
       args = parser.parse_args()
       print(f'Hello {args.name}')


def api_calendarific(BASE_URL):
       API_KEY = ''
       with open("token_crash.py") as file:
              API_KEY = file.read().strip()
       country= 'ES'
       year= '2019'
       res = requests.get("{}/holidays?&api_key={}&country={}&year={}".format(BASE_URL,API_KEY,country,year))
       res.json()
       lista = res.json()['response']['holidays']
       date=[]
       for elem in lista: 
              date.append(elem.get('date', 0).get('iso', 0)[:10]) 
              api_df=pd.DataFrame(date, columns = ["Date of public holidays in Spain"])
       return api_df

def plot_operator(crash):
       category_data= crash.operator.str.split('|', expand=True).stack().value_counts(0)/len(crash)*100
       category_data = category_data.round(1)
       category_data.head(5).plot('bar') 
       plt.title("Total crashes by operator")
       plt.savefig('Plot by operator')
       plt.show()

def plot_location(crash):
       category_data= crash.location.str.split('|', expand=True).stack().value_counts(0)/len(crash)*100
       category_data = category_data.round(1)
       category_data.head(5).plot('bar') 
       plt.title("Total crashes by location")
       plt.savefig('Plot by location')
       plt.show()
