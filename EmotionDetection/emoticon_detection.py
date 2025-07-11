import requests
import json

def emoticon_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Handle blank or empty input
    if not text_to_analyse or text_to_analyse.isspace():
        return {
            'anger': None, 
            'disgust': None,
            'fear': None, 
            'joy': None,
            'sadness': None, 
            'dominant_emotion': None
        }
    
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        # Send a POST request to the API with the text and headers
        response = requests.post(url, json=myobj, headers=header)
        
        # Check if the request was successful
        if response.status_code == 400:
            return {
                'anger': None, 
                'disgust': None,
                'fear': None, 
                'joy': None,
                'sadness': None, 
                'dominant_emotion': None
            }
        
        # Parse the JSON response
        formatted_response = json.loads(response.text)

        # Extract emotions from the nested structure
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Extract individual emotion scores
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger, 
            'disgust': disgust,
            'fear': fear, 
            'joy': joy,
            'sadness': sadness, 
            'dominant_emotion': dominant_emotion,
        }
    
    except Exception:
        # Handle any other unexpected errors
        return {
            'anger': None, 
            'disgust': None,
            'fear': None, 
            'joy': None,
            'sadness': None, 
            'dominant_emotion': None
        }