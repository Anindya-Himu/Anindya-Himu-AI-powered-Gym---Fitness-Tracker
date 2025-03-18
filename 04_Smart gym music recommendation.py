import random

def recommend_gym_music(mood):
    music = {
        "Energetic": ["Till I Collapse - Eminem", "Power - Kanye West", "Stronger - Daft Punk"],
        "Focused": ["Hans Zimmer - Time", "Alan Walker - Spectre"],
        "Relaxed": ["Chill Lofi Beats", "Deep House"]
    }
    return random.choice(music.get(mood, ["No mood detected"]))