import requests
import time
import re
import datetime
import json
import os

se = requests.session()

post_url = "https://global.ceair.com/portal/v3/flightStatus/queryFlightStatusByDate"

# current date
ti = datetime.datetime.now().strftime('%Y-%m-%d')

# necessary information for POST request
payloadData =  {
    "arrival": "SHA",
    "departure": "",
    "deviceId": "WHJMrwNw1k/FTPGYLNZaysfN2NQduAhAadM2TbE+4E950Zgv9GSYG8Sq1JD1zLPhvvv4Z6SIKaFwoCNX7PtF2v8lpBfEwBu3OfuhnGcEx8ia8PWTdb5FZGs5g8LyURrS6TZOJg5hGkZYfhwDCeHJsqFqRPoL7FhKirjl+d2XxfVgbmtlOj21pZoGQ/Ph4No66zbQCr3JAl5+QkT9kpOqV3YSaIMkkJKjw9LxxspH0OtncLjlxvuKHBUNguZ28MSymF10/rPYNoNw=1487582755342",
    "flightDate": ti,
    }
headers={'content-type': 'application/json'}

filename = '上海虹桥国际机场航班动态-中国东方航空数据 '+ti+'.json'
data = se.post(post_url,data=json.dumps(payloadData),headers=headers,verify=False).text
#print(data)
jsonData = json.loads(data).get('resultData')
result = []
# only take data we want
for item in jsonData:
    result.append({
        "flightDate":item.get('flightDate'),
        "flightNo":item.get("carrier")+item.get("flightNo"),
        "line":item.get("linezhs"),
        "statusCode":item.get("statusCode"),
        "deptAirport":item.get("deptAirport"),
        "arrAirport":item.get("arrAirport"),
        "planDeptTime":item.get("planDeptTime"),
        "realDeptTime":item.get("realDeptTime"),
        "planArrTime":item.get("planArrTime"),
        "realArrTime":item.get("realArrTime"),
        "terminal":item.get('aRR_TERMINAL')
    })


with open(filename,"w", encoding="utf-8") as f:
    f.write(json.dumps(result))
# os.system("scrapy crawl pkx")
# os.system('')
print("load data success! ",ti)