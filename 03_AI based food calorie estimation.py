import tensorflow as tf
import cv2
import numpy as np

def estimate_calories(image_path):
    model = tf.keras.models.load_model("models/food_calorie_model.h5")

    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224)) / 255.0
    image = np.expand_dims(image, axis=0)

    predicted_calories = model.predict(image)
    return predicted_calories[0][0]

# Example usage
calories = estimate_calories("food_image.jpg")
print(f"Estimated Calories: {calories} kcal")