import pandas as pd

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
       crash.rename(columns={'date':'Date'}, inplace=True)
       return crash