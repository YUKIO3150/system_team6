#テキストを入力で変更できるように
#キャラクターボイスの種類・速度を変更可能に
import requests
import json

url = 'http://localhost:50031/'
query_p = 'audio_query'
req_url = url + query_p
enable_interrogative_upspeak = ''


v_name = "test2.wav"
v_dir = "C:\\Users\\User\\DIR\\VOICE\\"　#自分のPythonの仮想環境パス
voice_pass = v_dir + v_name

#APIに送信する情報
speaker_id = 0　//キャラクターボイスの種類
#speaker_idには（重要）しゃべらせたいボイスのstyleIdを書いてください（上記はつくよみちゃんれいせいです）　
my_text = 'YHRくん'

headers = {'speaker':1}
q_params = {'text' :my_text,'speaker' :speaker_id, 'core_version':'0.0.0'}
a_params = {'speaker' :speaker_id, 'core_version':'0.0.0','enable_interrogative_upspeak' : 'true'}

#GETリクエストを送る
def Get_Request():
   response = requests.get(
   'http://localhost:50031/core_versions',
   )
   res_data = response.json()
   print(res_data)
   print(response.status_code)
   
#POSTリクエストを送る（クエリを作成）
def Post_RequestMQ():
   response = requests.post(req_url, params = q_params)
   res_data = response.json()
   #print(res_data)
   return res_data
 

#POSTリクエストを送る(音声合成し、返ってきた音声ファイルを保存)
def Post_RequestMA():
   response = requests.post('http://localhost:50031/synthesis',params = a_params,data= json.dumps(my_query))
   with open(voice_pass, 'wb') as saved_voice:
       saved_voice.write(response.content)

my_query = Post_RequestMQ()
#print(my_query)
Post_RequestMA()

#参考にしたサイト　https://note.com/npaka/n/n20763cb96cfb

