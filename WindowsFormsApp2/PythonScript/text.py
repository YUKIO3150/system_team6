import requests,os
import json,sys

headers = {
    'Authorization': "Bearer "+"7UWXHPoqEoAH0/3cZUXB5OhwaGrSTxkM2zl8AY9RDNhE8/Uuc88AjGFZRv0AiJcq1r/irTYRHtzMDM5oFEOoGWPzYIIteqpR8NQ0uRUFFDpbCUadDEzhVrxy3ypVofyvbw6yvloX8WZH/6rhKZrFpwdB04t89/1O/w1cDnyilFU=",
    'Content-Type': "application/json"
}

message = sys.argv[1]
audiourl ="https://drive.google.com/uc?id=1MIv4MTk2RoT6VMDpOkp0SzY3G8DTkpAQ"

res = requests.post("https://api.line.me/v2/bot/message/broadcast", 
    headers=headers, 
    json={
        "messages": [{
            "type": "text",
            "text": message}]
    }).json()

print(res)