from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get("textToAnalyze")
    analysis = emotion_detector(textToAnalyze)
    result = f"For the given statement, the system response is 'anger': {analysis['anger']}, 'disgust': {analysis['disgust']}, 'fear': {analysis['fear']}, 'joy': {analysis['joy']}, 'sadness': {analysis['sadness']}. The dominant emotion is {analysis['dominant_emotion']}."
    return result
