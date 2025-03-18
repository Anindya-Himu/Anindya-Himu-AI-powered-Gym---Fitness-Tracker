from flask import Flask, request, jsonify
from utils.music_recommendation import recommend_gym_music
from utils.location_finder import find_gym_nearby
from utils.reminders import send_reminders
from wearable_integration.smartwatch import get_smartwatch_data
from models.body_shape import analyze_body_shape, recommend_workout
from models.food_calories import estimate_calories

app = Flask(__name__)

@app.route('/recommend-music', methods=['GET'])
def music():
    mood = get_smartwatch_data()["mood"]
    return jsonify({"recommended_song": recommend_gym_music(mood)})

@app.route('/estimate-calories', methods=['POST'])
def food_calories():
    image = request.files['image']
    image_path = "uploads/food.jpg"
    image.save(image_path)
    return jsonify({"calories": estimate_calories(image_path)})

@app.route('/analyze-body', methods=['POST'])
def body_analysis():
    image = request.files['image']
    image_path = "uploads/body.jpg"
    image.save(image_path)
    body_type = analyze_body_shape(image_path)
    return jsonify({"body_type": body_type, "workout_suggestion": recommend_workout(body_type)})

if __name__ == '__main__':
    app.run(debug=True)