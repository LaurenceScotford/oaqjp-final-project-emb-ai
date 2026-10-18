"""Module for handling https requests to Emotion Detection API."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Renders index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Return emotion analysis for submitted text."""
    text_to_analyze = request.args.get("textToAnalyze")
    analysis = emotion_detector(text_to_analyze)
    if analysis["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    result = (
        f"For the given statement, the system response is "
        f"'anger': {analysis['anger']}, "
        f"'disgust': {analysis['disgust']}, "
        f"'fear': {analysis['fear']}, "
        f"'joy': {analysis['joy']}, "
        f"'sadness': {analysis['sadness']}. "
        f"The dominant emotion is {analysis['dominant_emotion']}."
    )
    return result
