import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=input_json,headers=headers)
    status_code = response.status_code

    all_emotions = {}

    if status_code == 200:
        json_response = json.loads(response.text)
        all_emotions = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(all_emotions, key=all_emotions.get)
        all_emotions['dominant_emotion'] = dominant_emotion
    elif status_code == 400:
        all_emotions['anger']=None
        all_emotions['disgust']=None
        all_emotions['fear']=None
        all_emotions['joy']=None
        all_emotions['sadness']=None
        all_emotions['dominant_emotion']=None
    return all_emotions