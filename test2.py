from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 設置您的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('ALV6KaH9KlvM6oCp1Xu6Y7fx3+b7PqAgsnP9iyCmwuiHG+JkX8G4BKmgc7suiLlaXrdcwH8rKnapyhsXoSab3jBdrmOps+uRlDtL2CpkMxu4SVJn9AE+HBlotvh/siShhCVNempzKZSm+OBoQoYZawdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1d2002486afe3e4db04318334b11cc83')

@app.route("/callback", methods=['POST'])
def callback():
    # 獲取 X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # 獲取請求的 body
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 驗證訊息
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
