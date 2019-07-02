import pandas as pd
import matplotlib.pyplot as plt
import calendarific
import requests
import numpy as np

def give_me_df(DataFrame):
       crash = pd.read_csv(DataFrame)
       return crash

def set_up(crash):
       colnames = ['location','operator','date']
       crash = pd.DataFrame(crash, columns=colnames)
       return crash

def date_clean(x): 
    months = {"January":1, "February":2, "March":3, "April":4, "May":5, "Jun":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}     
    for month, numero in months.items(): 
        if month in x: 
            mes = numero
    a = x.split(",")
    dia = a[0].split()[1]
    año = a[1].split()[0]
    return '{}-{}-{}'.format(dia, mes, año)

def data_clean(crash):
       crash = crash.drop_duplicates(subset=['operator', 'location','date']).dropna()
       crash.date = crash.date.apply(date_clean)
       crash = crash[crash['date'].str.contains('2018')]
       crash.rename(columns={'operator':'Operator'}, inplace=True)
       crash.rename(columns={'location':'Location'}, inplace=True)
       crash.rename(columns={'date':'Date'}, inplace=True)
       return crash

def plot_operator(crash):
    category_data= crash.operator.str.split('|', expand=True).stack().value_counts(0)/len(crash)*100
    category_data = category_data.round(1)
    category_data.head(5).plot('bar') 
    plt.title("Total crashes by operator")
    plt.savefig('Plot by operator')
    plt.show()

def plot_location(crash):
    category_data= crash.Location.str.split('|', expand=True).stack().value_counts(0)/len(crash)*100
    category_data = category_data.round(1)
    category_data.head(5).plot('bar') 
    plt.title("Total crashes by location")
    plt.savefig('Plot by location')
    plt.show()

def api_calendarific(BASE_URL):
       BASE_URL = "https://calendarific.com/api/v2"
       API_KEY = ''
       with open("token_crash.py") as file: # Use file to refer to the file object
              API_KEY = file.read().strip()
       country= 'ES'
       year= '2019'
       res = requests.get("{}/holidays?&api_key={}&country={}&year={}".format(BASE_URL,API_KEY,country,year))
       res.json()
       lista = res.json()['response']['holidays']
       date=[]
       for elem in lista: 
              date.append(elem.get('date', 0).get('iso', 0)[:10])  #.split(",")
              api_df=pd.DataFrame(date, columns = ["Date of public holidays in Spain"])
       return api_df
