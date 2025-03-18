import cv2
import numpy as np
import tensorflow as tf

def analyze_body_shape(image_path):
    model = tf.keras.models.load_model("models/body_shape_model.h5")

    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224)) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    classes = ["Ectomorph", "Mesomorph", "Endomorph"]
    
    body_type = classes[np.argmax(prediction)]
    return body_type

def recommend_workout(body_type):
    workouts = {
        "Ectomorph": "Strength training, compound lifts, high-calorie diet.",
        "Mesomorph": "Balanced strength & cardio for definition.",
        "Endomorph": "HIIT workouts, calorie control."
    }
    return workouts.get(body_type, "Unknown body type")