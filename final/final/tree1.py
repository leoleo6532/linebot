#linebotTest1
from flask import Flask
app = Flask(__name__)

#import flask
from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage , ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction, ImageMessage
#使用者Channel access token
line_bot_api = LineBotApi('Hc90MUcu0Q8piJp9GH6MDTq2f43u1meU0waergNPejOzZEL0guy7YOd8XEPSCU98amxYZ1Mtxhxgz6fJL/RJxflgTCyK83uASy5l3s2qYwa+1Wiww1LTd9EryeA6B+JHxIUfFpeXGOEkte8Dk1A24wdB04t89/1O/w1cDnyilFU=')
#使月者Channel secret
handler = WebhookHandler('10fad983e230a499c2668ee16ecd4691')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    #獲得使用者輸入的訊息
    body = request.get_data(as_text=True)
    try:
        #送出訊息
        handler.handle(body, signature)
    except InvalidSignatureError:
        #送出Bad request (400)
        abort(400)
    
    #回覆OK
    return 'ok'


@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    # 請api回覆已經上傳
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Image has Upload'+ ' ' + event.message.id))
    
    # 請api用get_message_content依照消息id將照片要回
    message_content = line_bot_api.get_message_content(event.message.id)
    
    # 存起來
    with open('D:/產業尖兵/Python_project/tutorial/0819/gallery/'+event.message.id+'.jpg', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)



if __name__ == '__main__':
    app.run()            