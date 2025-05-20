"""
Flask application for emotion detection web service.

This module provides a web interface for analyzing the emotions
in a given text using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection import emoticon_detector

APP = Flask(__name__)

def render_index_page():
    """
    Render the main index page of the application.

    Returns:
        flask.Response: Rendered HTML template for the index page.
    """
    return render_template('index.html')

def sent_analyzer():
    """
    Analyze the sentiment of the provided text.

    Retrieves text from GET request, processes it through emotion detector,
    and returns a formatted response string.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    # Retrieve text to analyze from GET request
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Get emotion analysis results
    response = emoticon_detector(text_to_analyze)
    
    # Check if dominant emotion is None (indicating an error)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the output as requested
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is **{response['dominant_emotion']}**."
    )
    
    return output_string

# Configure routes
APP.route("/")(render_index_page)
APP.route("/emotionDetector", methods=['GET'])(sent_analyzer)

def main():
    """
    Main entry point for running the Flask application.

    Starts the web server on localhost port 5000.
    """
    APP.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()