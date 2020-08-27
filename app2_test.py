import requests
import datetime
import pytz
import os
import time
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET  
def monoNim(n):
    content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
    tree = ET.fromstring(content.text)
    items = list(tree.iter(tag = 'item'))
    title = items[n][0].text
    ptext = items[n][2].text
    ptext = ptext.replace('<p>','').replace('</p>','\n')
    return title +'月\n' + ptext[:-1]

#print(monoNim(0))    #本期


#print(monoNim(1) + monoNim(2))    #前期
content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
tree = ET.fromstring(content.text)
items = list(tree.iter(tag = 'item'))
title = items[0][0].text
ptext = items[0][2].text


zz = ptext[43:69]
za = ptext[12:15]
zb = ptext[30:33]
#print(zz[5:8],zz[14:17],zz[23:26])
print(zb)
print(str(datetime.datetime.now())[:19])


while(1):
 path = 'C:\\Last_test\\DL\\MAIN\\AI_TEST\\sick'
 count = 0
 for root,dirs,files in os.walk(path):    #遍历统计
      for each in files:
          if each.endswith('jpg'):
             count += 1   #统计文件夹下文件个数
 time.sleep(0.5)
 print ("文件的总数量为：",count)
