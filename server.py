from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analysis():
    text_for_analysis = request.args.get('textToAnalyze')
    emotion_results = emotion_detector(text_for_analysis)
    if emotion_results['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    else:
        return f"For the given statement, the system response is 'anger': {emotion_results['anger']}, 'disgust': {emotion_results['disgust']}, 'fear': {emotion_results['fear']}, 'joy': {emotion_results['joy']}, 'sadness': {emotion_results['sadness']}. The dominant emotion is {emotion_results['dominant_emotion']}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)