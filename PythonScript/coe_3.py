import requests
import json
import sys

url = 'http://localhost:50031/'
query_p = 'accent_phrases'#audio_query
req_url = url + query_p
enable_interrogative_upspeak = ''


v_name = "test.wav"
v_dir = "C:\\Users\\daiki\\test\\"
voice_pass = v_dir + v_name

# APIに送信する情報

my_text = sys.argv[1]
speaker_id = int(sys.argv[2])
#speaker_idにはしゃべらせたいボイスのstyleId

my_speed = int(sys.argv[3])
#speed：話速 0.5 < 1 < 2

my_pitch = 0
#pitch:音高(音質劣化) -0.15 < 0 < 0.15

my_intonation = int(sys.argv[4])
#intonation:抑揚(音質劣化) 0 < 1 < 2

my_volume = 1
#volume:音量 0 < 1 < 2

my_pre_L = 0.1
#pre_L:開始無音 0 < 0.1 < 1.5

my_post_L = 0.1
#post_L:終了無音 0 < 0.1 < 1.5

headers = {'speaker':1}
q_params = {'text' :my_text,
            'speaker' :speaker_id,
            'kana' :False,
            'core_version':'0.0.0'}

a_params = {'speaker' :speaker_id, 
            'core_version':'0.0.0',
            'enable_interrogative_upspeak' : 'true'}


#print(json.dumps(json_data))
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
   response1 = requests.post(req_url, params = q_params)
   res_data1 = response1.json()
   response = {
       'accent_phrases': res_data1,
       'speedScale': my_speed,
       'pitchScale': my_pitch,
       'intonationScale': my_intonation,
       'volumeScale': my_volume,
       'prePhonemeLength' : my_pre_L,
       'postPhonemeLength': my_post_L,
       'outputSamplingRate': 44100,
       'outputStereo': False
        }
   res_data = response
   #print(res_data)
   #print(response.status_code)
   return res_data
 

#POSTリクエストを送る(音声合成し、返ってきた音声ファイルを保存)
def Post_RequestMA():
   response = requests.post('http://localhost:50031/synthesis',
                            params = a_params,data= json.dumps(my_query))
   with open(voice_pass, 'wb') as saved_voice:
       saved_voice.write(response.content)
   print(response.status_code)

my_query = Post_RequestMQ()
#print(my_query)
Post_RequestMA()
