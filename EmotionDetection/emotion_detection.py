import requests
import json

def emotion_detector(text_to_analyze):
    """
    Perform emotion detection on the given text using a remote API.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and dominant emotion.
            Keys:
                - 'anger': The intensity of anger emotion.
                - 'disgust': The intensity of disgust emotion.
                - 'fear': The intensity of fear emotion.
                - 'joy': The intensity of joy emotion.
                - 'sadness': The intensity of sadness emotion.
                - 'dominant_emotion': The dominant emotion in the text.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=obj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
 
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return output

