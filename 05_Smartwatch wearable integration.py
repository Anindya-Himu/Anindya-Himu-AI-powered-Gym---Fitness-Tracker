import random

def get_smartwatch_data():
    heart_rate = random.randint(60, 140)
    temperature = round(random.uniform(36.0, 38.5), 1)
    bp = (random.randint(100, 140), random.randint(60, 90))
    movement = random.randint(0, 100)  # Activity level

    mood = "Relaxed"
    if heart_rate > 120:
        mood = "Energetic"
    elif movement > 50:
        mood = "Focused"

    return {"heart_rate": heart_rate, "temperature": temperature, "bp": bp, "mood": mood}

# Example Usage
tracker_data = get_smartwatch_data()
print(f"Smartwatch Data: {tracker_data}")