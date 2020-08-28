from flask import Flask, request, abort
from urllib.request import urlopen
from flask import Flask, request, abort
from urllib.request import urlopen
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import *
from numpy import *
import time  
import sys    
import datetime
import requests
import time
import json 
import os
import pytz 
import random   
import os 
from linebot.models import MessageEvent, TextMessage, TextSendMessage , ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ImageMessage
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET  
#****************************************************************************    
def monoNim(n):
    content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
    tree = ET.fromstring(content.text)
    items = list(tree.iter(tag = 'item'))
    title = items[n][0].text
    ptext = items[n][2].text
    ptext = ptext.replace('<p>','').replace('</p>','\n')
    return title +'月\n' + ptext[:-1]    
#****************************************************************************
content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
tree = ET.fromstring(content.text)
items = list(tree.iter(tag = 'item'))
title = items[0][0].text
ptext = items[0][2].text
zz = ptext[43:69]
za = ptext[12:15]
zb = ptext[30:33]
#*************************************************************************

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('4kCucQHbafhioRCGd6OjavjokDZ2JaG3LJZms7BNveH6eX9MXo3wJk6KHwrE+qLkKGQd7L3Nk3FrXa9aku5yubwLNIXpapd77gwMsgU4vk6IXsP1FopoWp4LCBCh7p4K5kaLWVrb/McCkUVFmpgmoAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5528cc7a9bdf5e1409229fb503d65ac5')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event): 
    #總通道
    deviceID = '17750119494' 
    apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceID + '/rawdata'
    headers = { 
    "CK":"PK0B9PPBEHGEA4ASC7",
    "Content-Type": "application/json",
    } 


    
    print(event)
    text=event.message.text
    if (text=="hi"):
        today=str(datetime.date.today())
        UTC = str(datetime.datetime.utcnow())[11:23]  
        reply_text = "Hello "+today
        print(text)
        #Your user ID

    elif (text=="團隊資訊"):
        reply_text = "http://192.168.43.51/index1.php"      

    elif (text=="@本期中獎號碼"):
        reply_text = monoNim(0)

    elif (text=="@前期中獎號碼"):
        try:
           message = [
              TextSendMessage(
              text = monoNim(1)
             ),
              TextSendMessage(
              text = monoNim(2)
             )
           ]
           line_bot_api.reply_message(event.reply_token,message)
        except:
           line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤"))    
    elif (text=="@輸入發票最後三碼"):  
         reply_text = "請輸入發票末三碼"   



    elif( "圖片"  in  text):
        try:
           message = ImageSendMessage(
              original_content_url = "https://i.imgur.com/LNwfaQL.jpg",
              preview_image_url = "https://i.imgur.com/LNwfaQL.jpg"
           )
           line_bot_api.reply_message(event.reply_token,message)
        except:
           line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤"))
    elif( "瀚元"  in  text):
        try:
            message = [
             TextSendMessage(
              text = "瀚元牛逼~~"
             ),
             StickerSendMessage(
              package_id =  "1",
              sticker_id = "14"
             )
            ]
            line_bot_api.reply_message(event.reply_token,message)
        except:
           line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤"))


    elif( "介紹"  in  text):
        try:
           message = [

              TextSendMessage(
              text = "我害羞~~"
             ),
              ImageSendMessage(
              original_content_url = "https://i.imgur.com/LNwfaQL.jpg",
              preview_image_url = "https://i.imgur.com/LNwfaQL.jpg"             
             ),
              StickerSendMessage(
              package_id =  "2",
              sticker_id = "522"
             )   

           ]
           line_bot_api.reply_message(event.reply_token,message)
        except:
           line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤"))           

    elif( "醫院"  in  text):
        try:
           message = [
              TextSendMessage(
              text = "臺大醫院網址:\nhttps://www.ntuh.gov.tw/ntuh/Index.action"
             ),
              LocationSendMessage(
              title='臺大醫院',
              address="No. 7, Zhongshan South Road, Zhongzheng District, Taipei City, 100",
              latitude=25.0407,
              longitude=121.5190
             )
           ]           
           line_bot_api.reply_message(event.reply_token,message)
        except:
           line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤"))


    elif( "快速選單"  in  text):
        try:
          message = TextSendMessage(
              text = "請選擇最喜歡的程式語言",
              quick_reply=QuickReply(
                items = [
                      QuickReplyButton(
                        action = MessageAction(label="python",text="python")
                    ),
                      QuickReplyButton(
                        action = MessageAction(label="java",text="java")
                    ),    
                     QuickReplyButton(
                       action = MessageAction(label="C#",text="c#")
                    ),   
                    QuickReplyButton(
                       action = MessageAction(label="c++",text="c++")
                    )                                          
                  ]
               )
              )   
                  
          line_bot_api.reply_message(event.reply_token,message)
        except:
          line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤"))


    elif(text=="可查詢" or text=="功能" or text=="?"): 
        reply_text = "本產品[肺-REAL-GOOD]官方網址如下:\nhttp://192.168.43.51/index1.php\n功能列表:\n***最新10筆資料***\n1.顯示病患檢測時間\n2.顯示病患ID及預測得病率\n3.可上傳影像立即辨識\n聯絡電話:02-2234-2258\nEmail:zxcv@gmail.com"   
    elif( "肺癌"  in  text):
        apiURL= 'https://iot.cht.com.tw/iot/v1/device/23632626264/sensor/data2/rawdata?start=2020-08-19T23:59:59.000Z&end=2020-12-31T23:59:59.000Z&utcOffset=8'  #大平台通道ID  &utcOffset=8
        headers = {
                    "CK":"PK4ACRESYYKAKUUTPE",
                    "Content-Type": "application/json",
                   }
        payload=[{"id":"data2"}]
        response1 = requests.get(apiURL, headers=headers, data=json.dumps(payload))
        hjson = json.loads(response1.text)
        #reply_text = "預約掛號網址:http://localhost/index1.php"
        try:  
          get_date1 = (hjson[-1]['time'],hjson[-1]['value'])
          get_date2 = (hjson[-2]['time'],hjson[-2]['value'])
          get_date3 = (hjson[-3]['time'],hjson[-3]['value'])
          get_date4 = (hjson[-4]['time'],hjson[-4]['value'])
          get_date5 = (hjson[-5]['time'],hjson[-5]['value'])
          get_date6 = (hjson[-6]['time'],hjson[-6]['value'])
          get_date7 = (hjson[-7]['time'],hjson[-7]['value'])
          get_date8 = (hjson[-8]['time'],hjson[-8]['value'])
          get_date9 = (hjson[-9]['time'],hjson[-9]['value'])
          get_date10 = (hjson[-10]['time'],hjson[-10]['value'])
          reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)+"\n"+str(get_date5)+"\n"+str(get_date6)+"\n"+str(get_date7)+"\n"+str(get_date8)+"\n"+str(get_date9)+"\n"+str(get_date10)
        except: 
         try:   
            reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)+"\n"+str(get_date5)+"\n"+str(get_date6)+"\n"+str(get_date7)+"\n"+str(get_date8)+"\n"+str(get_date9)
         except: 
            try:  
              reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)+"\n"+str(get_date5)+"\n"+str(get_date6)+"\n"+str(get_date7)+"\n"+str(get_date8)
            except:
              try:  
               reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)+"\n"+str(get_date5)+"\n"+str(get_date6)+"\n"+str(get_date7)
              except: 
                try:  
                  reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)+"\n"+str(get_date5)+"\n"+str(get_date6) 
                except: 
                    try:
                      reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)+"\n"+str(get_date5)
                    except: 
                      try:  
                        reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)+"\n"+str(get_date4)  
                      except: 
                       try:    
                         reply_text = str(get_date1)+"\n"+str(get_date2)+"\n"+str(get_date3)
                       except:
                           try: 
                             reply_text = str(get_date1)+"\n"+str(get_date2)
                           except:
                             reply_text = str(get_date1)
    else:
        pass
     
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)        

#發票兌獎
'''
    else:
        if(len(text) != 3):
          reply_text ="請輸入發票最後三碼"
        else:
          if(text == zz[5:8] or text == zz[14:17] or text == zz[23:26] or  text == za or text == zb):
              try:
                        message = [
                        TextSendMessage(
                        text = "符合某獎項後三碼請自行核對前五碼"
                        ),  
                        TextSendMessage(
                        text = monoNim(0)
                        )                        
                        ]
                        line_bot_api.reply_message(event.reply_token,message)
              except:
                        line_bot_api.reply_message(event.reply_token,message,TextSendMessage(reply_text = "發生錯誤")) 
          else:
              reply_text ="可惜未中獎"                
'''
#圖片辨識
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    time.sleep(6)
    # 存起來
    with open('C:\\Last_test\\DL\\MAIN\\AI_TEST\\sick\\'+event.message.id+'.jpg', 'wb') as fd:
        for chunk in message_content.iter_content():#照片太大可以支援
            fd.write(chunk)      
    apiURL= 'https://iot.cht.com.tw/iot/v1/device/23632626264/sensor/data2/rawdata?start=2020-08-19T23:59:59.000Z&end=2020-12-31T23:59:59.000Z&utcOffset=8'  #大平台通道ID  &utcOffset=8
    headers = {
                "CK":"PK4ACRESYYKAKUUTPE",
                "Content-Type": "application/json",
              }
    payload=[{"id":"data2"}]
    response1 = requests.get(apiURL, headers=headers, data=json.dumps(payload))
    hjson = json.loads(response1.text) 
    get_data = (hjson[-1]['time'],hjson[-1]['value'])
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = str(get_data)))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)