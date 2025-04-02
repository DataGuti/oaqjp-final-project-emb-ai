"""
Emotion Detection Server File

This Python script handles the Flask server and connects to the EmotionDetection object.

"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analysis():
    """
    This is the main function to run the emotion analysis.
    It connects to the EmotionDetection.emotion_detector function.
    Takes a string as input, returns a JSON object as result.
    This JSON object has a score for each emotion and a dominant_emotion for the text.
    """
    text_for_analysis = request.args.get('textToAnalyze')
    emotion_results = emotion_detector(text_for_analysis)
    if emotion_results['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (
        f"For the given statement, the system response is 'anger': {emotion_results['anger']}, "
        f"'disgust': {emotion_results['disgust']}, 'fear': {emotion_results['fear']}, "
        f"'joy': {emotion_results['joy']}, 'sadness': {emotion_results['sadness']}. "
        f"The dominant emotion is {emotion_results['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    This function renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
