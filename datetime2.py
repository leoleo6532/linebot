import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from selenium import webdriver
import sys    
import datetime
import json 
import os
while(2>1):
  pageRequest = requests.get('https://www.naif.org.tw/infoPigSellDaily.aspx')
  soup = BeautifulSoup(pageRequest.content, 'html.parser')
  soup.encoding = 'utf-8'
  pigpig = soup.find(attrs={"class":"ScrollForm"}).text
  print(pigpig)
  time.sleep(60*5)