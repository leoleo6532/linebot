import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from selenium import webdriver
import sys    
import datetime
import json 
import os


deviceID = '18396174048' 
apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceID + '/rawdata'
headers = { 
    "CK":"PKGE0WGKTSUFZWPCHK",
    "Content-Type": "application/json",
} 


def all():
 url = 'https://www.cwb.gov.tw/V7/forecast/txt/w50.htm'
 driver =  webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
 driver.get(url)
 soup = BeautifulSoup(driver.page_source,'html.parser')
 content = ""
 a = ""
 try:
     for data in soup.select('#mydata'):
         title = str(data)
         for weather in range(1,10):
             content = title.split("<br/><br/>")[weather]
 except:
         weather2 = weather-2    
         for weather3 in range(weather2):
             content123 = title.split("<br/><br/>")[weather3]
             a += content123
         return a    
#print(all()[112:])   

while True:
    payload=[{"id":"all", "value":[all()[112:]]}]  
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
    print(payload)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(60*5)


