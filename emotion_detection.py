import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    text_to_analyze = text_to_analyze.strip()
    if text_to_analyze == "":
        return "Invalid parameters: Please send a non-zero length string!", 400

    input_json = {
        "raw_document": {"text": text_to_analyze}
    }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        return response.text, 500

    return "A server error occurred and your request could not be processed!", 500
