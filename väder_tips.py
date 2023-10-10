import requests
import datetime
import openpyxl

url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json'


väder_data = requests.get(url)

# print(type(väder_data.json()))
ny_väder_data = väder_data.json()

# for key in ny_väder_data:
#     print(key)

print(type(ny_väder_data['timeSeries']))
print(len(ny_väder_data['timeSeries']))
# print((ny_väder_data['timeSeries'][0]['parameters']))

for data in (ny_väder_data['timeSeries']):
    for p in data['parameters']:
        if p['name'] == 'pcat':
            if p['values'][0] == 0:
                print('Ingen nederbörd')
            else:
                print('Nederbörd')

lista_med_datetime = []

# for dictionary in ny_väder_data['timeSeries'][:24]:
#     tid = dictionary["validTime"].replace('Z','')
#     ny_tid = datetime.datetime.strptime(tid,'%Y-%m-%dT%H:%M:%S')
#     print(ny_tid.hour)


new = openpyxl.Workbook()