#coding:UTF-8
import requests,os

#------画像を送る場合----------------------------
def main_gazo():
    url = "https://notify-api.line.me/api/notify"
    token = "BT6DgLy1TO1VBoBV2OYhkIgzDtYwTudtFhrNjQpDG6Z"
    headers = {"Authorization" : "Bearer "+ token}

    message = ' '
    payload = {"message" :  message}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open('001.jpg','rb')}
    #rbはバイナリファイルを読み込む
    post = requests.post(url ,headers = headers ,params=payload,files=files)


#------メッセージを送る場合----------------------------
def main():
    url = "https://notify-api.line.me/api/notify"
    token = "gttp0LRwrLZCJE6cYDqgt8KryEvOYNTNpxFhGUhGgQc"
    headers = {"Authorization" : "Bearer "+ token}

    message = 'Fortnite！'
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)


if __name__ == '__main__':
    main_gazo()#画像を送るmain_gazo()を動かしてみる（メッセージの場合はmain()）