"""
Emotion Detection Web Application

This Flask application provides a simple web interface for emotion detection using
a pre-trained emotion detection model.

Usage:
- Navigate to the root URL '/' to access the web interface.
- Send a GET request to '/emotionDetector' with a query parameter 'textToAnalyze' containing
  the text to analyze for emotions. The response will be a JSON object containing emotion scores.

Author: Mohamed Ali

"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def em_detector():
    """
    Endpoint for emotion detection.

    This endpoint receives a text input through a query parameter 'textToAnalyze',
    analyzes the emotion in the text, and returns the results in JSON format.

    Returns:
        JSON response containing emotion scores for the given text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {output['anger']}, "
        f"'disgust': {output['disgust']}, "
        f"'fear': {output['fear']}, "
        f"'joy': {output['joy']} and "
        f"'sadness': {output['sadness']}. "
        f"The dominant emotion is {output['dominant_emotion']}."
    )
    return jsonify(response_text)

@app.route('/')
def index():
    """
    Home page.
    Renders the index.html template, which contains the web interface.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
