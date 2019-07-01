import pandas as pd
import matplotlib.pyplot as plt

def read(DataFrame):
       crash = pd.read_csv(DataFrame)
       return crash

def set_up(crash):
       colnames = ['location','operator','date']
       crash = pd.DataFrame(crash, columns=colnames)
       return crash

def data_clean(crash):
       crash = crash.sort_values(by='date', ascending=False)
       crash = crash.drop_duplicates(subset=['operator', 'location','date']).dropna()
       crash = crash["date"].str.split(" ", n = 1, expand = True)
       crash = crash[1].str.split(",", n = 1, expand = True)
       crash["Crashes days"]=crash[0]
       crash["Crashes years"]=crash[1]
       crash = crash.filter(["Crashes days","Crashes years"], axis=1)
       crash = crash.drop(crash[crash['Crashes years']!='2018'].index)
       crash["Crashes months"]=crash[0]
       month_df=crash["Crashes months"]
       month_df=pd.DataFrame(month_df, columns = ["Crashes months"])

       def findMonth (m):
              months = {
              "January":1, "February":2, "March":3, "April":4, "May":5, "Jun":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12
              }
              for month, numero in months.items(): 
                     if month in m: 
                            return numero
              return None
       month_crash["Crashes months"] = month_crash["Crashes months"].apply(findMonth)
       ["Crashes days"]=crash[0]
       crash["Crashes years"]=crash[1]
       new1 = new1.filter(["Crashes days","Crashes years"], axis=1)
       crash.rename(columns={'date':'Date'}, inplace=True)
       crash.rename(columns={'operator':'Operator'}, inplace=True)
       crash.rename(columns={'location':'Location'}, inplace=True)
       return crash

def plot_operator(crash):
    category_data= crash.Operator.str.split('|', expand=True).stack().value_counts(0)/len(crash)*100
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

def api_calendarific(API_KEY):
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


#def plot_date(crash):
 #   category_data= crash.Date.str.split('|', expand=True).stack().value_counts(0)/len(crash)*100
  #  category_data = category_data.round(1)
   # category_data.head(5).plot('bar') 
   # plt.title("Total crashes by date")
   # plt.savefig('Plot by date')
#plt.show()

