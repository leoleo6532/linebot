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

while(2>1):
  pageRequest = requests.get('http://ppg.naif.org.tw/naif/MarketInformation/Reference/reference.aspx')
  soup = BeautifulSoup(pageRequest.content, 'html.parser')
  soup.encoding = 'utf-8'
  pigpig = soup.find(attrs={"class":"tbNews"}).text
  pigpig2 = pigpig.replace("\n","")
  pigpig3 = pigpig2.replace("\xa0","")
  payload=[{"id":"linepig", "value":[pigpig3]}] 
  response = requests.post(apiURL, headers=headers, data=json.dumps(payload)) 
  print(payload)
  time.sleep(60*5)
