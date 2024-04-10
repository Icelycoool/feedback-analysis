from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)
    
    # Constructing the response in the desired format
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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)