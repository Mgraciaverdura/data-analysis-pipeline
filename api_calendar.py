import calendarific
import requests

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
print(date)

df=pd.DataFrame(date, columns = ["Date of public holidays in Spain"])
display(df)

#holidays?&api_key=baa9dc110aa712sd3a9fa2a3dwb6c01d4c875950dc32vs&country=US&year=2019
#https://calendarific.com/api/v2/holidays?&api_key=baa9dc110aa712sd3a9fa2a3dwb6c01d4c875950dc32vs&country=US&year=2019
#print(res)
#calapi = calendarific.v2(API_KEY)
#parameters = {
	# Required
#	'country': 'ES',
#	'year': '2019',
#}
#holidays = calapi.holidays(parameters)