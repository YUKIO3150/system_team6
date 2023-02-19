#coding:UTF-8
import requests,os

#------画像を送る場合----------------------------
def main_gazo():
    url = "https://notify-api.line.me/api/notify"
    token = "7UWXHPoqEoAH0/3cZUXB5OhwaGrSTxkM2zl8AY9RDNhE8/Uuc88AjGFZRv0AiJcq1r/irTYRHtzMDM5oFEOoGWPzYIIteqpR8NQ0uRUFFDpbCUadDEzhVrxy3ypVofyvbw6yvloX8WZH/6rhKZrFpwdB04t89/1O/w1cDnyilFU="
    headers = {"Authorization" : "Bearer "+ token}

    message = ' '
    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open('001.jpg','rb')}
    #rbはバイナリファイルを読み込む
    post = requests.post(url ,headers = headers ,params=payload,files=files)


#------メッセージを送る場合----------------------------
def main():
    url = "https://api.line.me/v2/bot/message/push"
    token = "7UWXHPoqEoAH0/3cZUXB5OhwaGrSTxkM2zl8AY9RDNhE8/Uuc88AjGFZRv0AiJcq1r/irTYRHtzMDM5oFEOoGWPzYIIteqpR8NQ0uRUFFDpbCUadDEzhVrxy3ypVofyvbw6yvloX8WZH/6rhKZrFpwdB04t89/1O/w1cDnyilFU="
    headers = {"Authorization" : "Bearer "+ token}

    message = 'Fortnite！'
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)


#------音声を送る場合----------------------------
def main_onsei():
    url = "https://notify-api.line.me/api/notify"
    token = "BT6DgLy1TO1VBoBV2OYhkIgzDtYwTudtFhrNjQpDG6Z"
    headers = {"Authorization" : "Bearer "+ token}

    message = ' '
    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open("C:\Users\user\Desktop\WindowsFormsApp2\PythonScript\test.wav",'rb')}
    #rbはバイナリファイルを読み込む
    post = requests.post(url ,headers = headers ,params=payload,files=files)

if __name__ == '__main__':
    main()#画像を送るmain_gazo()を動かしてみる（メッセージの場合はmain()）