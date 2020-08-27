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

def Taipei():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm'
    driver =  webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    content = ""
    for data in soup.select('#ftext'):
        title = str(data)
        content = title.split("<br/><br/>")[2]
    return content

def Yilan():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Yilan_County.htm'
    driver =  webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    content = ""
    for data in soup.select('#ftext'):
        title = str(data)
        content = title.split("<br/><br/>")[2]
    return content    
    
while True:
    payload=[{"id":"Taipei", "value":[Taipei()]}]    
    payload2=[{"id":"Yilan", "value":[Yilan()]}] 
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
    response2 = requests.post(apiURL, headers=headers, data=json.dumps(payload2))
    print(payload)  
    print(payload2)  
    time.sleep(60*5)
    