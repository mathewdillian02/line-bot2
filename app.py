import os                          
from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent

app = Flask(__name__)

# Replace with your actual credentials from the LINE Developers Console
configuration = Configuration(access_token='awXQa5SDbERn7bO27T+FXFMZ5kXxs+Mxr7aY2v/zuD6jAlWjZLB9AMCMAtwbfVvD4gEc9VXrrrMN8/VA+0nzy3dc+ez/RL7V40N8croZXcpKO4DPzJrq8iJ5y4CWqrqjT5w9qVGpazIeBNZcSr5bXAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6c3c4cdb4b604aef2dbdda4d52074003')
@app.route("/")
def home():
    return "bot is running"
@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

from linebot.v3.webhooks import MessageEvent, TextMessageContent
CONF = Configuration(access_token='awXQa5SDbERn7bO27T+FXFMZ5kXxs+Mxr7aY2v/zuD6jAlWjZLB9AMCMAtwbfVvD4gEc9VXrrrMN8/VA+0nzy3dc+ez/RL7V40N8croZXcpKO4DPzJrq8iJ5y4CWqrqjT5w9qVGpazIeBNZcSr5bXAdB04t89/1O/w1cDnyilFU=')
HANDLER = WebhookHandler('a505a22b0063d6e9bf61b1e655617ca2')
ADMIN_ID = 'U195b384a10e29369b0a3737d860a5994'


