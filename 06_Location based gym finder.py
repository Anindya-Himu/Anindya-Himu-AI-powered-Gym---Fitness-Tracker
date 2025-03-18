import requests

def find_gym_nearby(location):
    api_key = "YOUR_GOOGLE_PLACES_API_KEY"
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=5000&type=gym&key={api_key}"
    
    response = requests.get(url)
    gyms = response.json()
    
    for gym in gyms['results'][:5]:
        print(f"🏋️ Gym: {gym['name']}, Location: {gym['vicinity']}")

# Example
find_gym_nearby("60.1699,24.9384")  # Helsinki