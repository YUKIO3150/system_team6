
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import AudioSendMessage

    
bot_api = LineBotApi('8ZVbKVuSLI0ZImH8ZXhcXNdNPcPkxc8N/dpJwmg6MLK2r3a8wCK0rGWkTFgBQpCgBMgB9M1dPaoaavWQ3vSHCiB4S2DgVXsCGRwYebJCOxU+t1u2oNHDMj6bth5nBWLruJ1icXw9rX4pjgFfP4c4nwdB04t89/1O/w1cDnyilFU=') #トークン

def main():
    user_id = 'U6da319863129347e287c0fffcbfaf65e' #ID
    audio_message = AudioSendMessage(
        original_content_url='https://s33.aconvert.com/convert/p3r68-cdx67/n6b1c-mzpnk.m4a' ,  #ファイルURL　　https://**********.m4a
        duration=60000  #音声の長さの最大(ms)
        ) #LINEに送付するメッセージ
    bot_api.push_message(user_id, messages=audio_message)
    
main() #メイン関数を実行

#line-bot-adk  が必要