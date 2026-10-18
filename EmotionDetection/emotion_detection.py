import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = {
        "raw_document": {"text": text_to_analyze}
    }

    response = requests.post(url, headers=headers, json=input_json)
    
    json_obj = response.json()

    emotion_scores = json_obj["emotionPredictions"][0]["emotion"]
    result = {
        "anger": float(emotion_scores["anger"]),
        "disgust": float(emotion_scores["disgust"]),
        "fear": float(emotion_scores["fear"]),
        "joy": float(emotion_scores["joy"]),
        "sadness": float(emotion_scores["sadness"])
    }
        
    largest = 0
    dominant = ""
    for key, value in result.items():
        if value > largest:
            largest = value
            dominant = key

    result["dominant_emotion"] = dominant

    return result

