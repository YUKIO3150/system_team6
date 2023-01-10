import requests
import PIL
import pydub
import os
import cv2
import io
from io import BytesIO
import numpy as np
from pathlib import Path
import struct
from PIL import Image

#必要な変数を設定
#取得したトークン
TOKEN = 'gttp0LRwrLZCJE6cYDqgt8KryEvOYNTNpxFhGUhGgQc'
#APIのURL
api_url = 'https://notify-api.line.me/api/notify'
#送りたい内容
#image_file = cv2.imread(r"C:\Users\user\DIR\001.jpg",2)
image_file="C:\\Users\\user\\DIR\\001.jpg"

#class ImgByteChange:
    #def __init__(self):
        #pass
    #def ImageToByte(self,Img):
        #tmpimg = Image.open(Img)
        #with io.BytesIO() as output:
            #tmpimg.save(output,format="PNG")
            #ImgToByte = output.getvalue()
            #return ImgToByte
    
#imgByteChange = ImgByteChange()
#test = imgByteChange.ImageToByte(image_file)

#c = base64.encodestring(open(fname, 'rb').read())
img = Image.open(image_file)
with open(image_file, 'rb') as f:
    binary = f.read()
img = Image.open(BytesIO(binary))
#ret,bi_img = cv2.threshold(image_file, 127, 255, cv2.THRESH_BINARY)
#binary = cv2.threshold(image_file, 127, 255, cv2.THRESH_BINARY)
#cv2.imshow("Binary", bi_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
image_dic = {"imageFile": binary}
#LINE通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
print(TOKEN_dic)
print(binary)
requests.post(api_url, headers=TOKEN_dic, files=image_dic)

