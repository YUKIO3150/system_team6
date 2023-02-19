
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import AudioSendMessage

    
bot_api = LineBotApi('77UWXHPoqEoAH0/3cZUXB5OhwaGrSTxkM2zl8AY9RDNhE8/Uuc88AjGFZRv0AiJcq1r/irTYRHtzMDM5oFEOoGWPzYIIteqpR8NQ0uRUFFDpbCUadDEzhVrxy3ypVofyvbw6yvloX8WZH/6rhKZrFpwdB04t89/1O/w1cDnyilFU=') #トークン

def main():
    user_id = 'yukio3150ittyateru' #ID
    audio_message = AudioSendMessage(
        original_content_url='https://drive.google.com/uc?id=1MIv4MTk2RoT6VMDpOkp0SzY3G8DTkpAQ&m4a' ,  #ファイルURL　　https://**********.m4a
        duration=60000  #音声の長さの最大(ms)
        ) #LINEに送付するメッセージ
    bot_api.push_message(user_id, messages=audio_message)
    
main() #メイン関数を実行

#line-bot-adk  が必要