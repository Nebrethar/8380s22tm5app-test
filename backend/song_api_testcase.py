import requests

def test_random_song():
    random_song = requests.get("https://8380s22tm5app.com/random-song/")
    return random_song.status_code==200

def test_weather_song():
    weather_song = requests.get("https://8380s22tm5app.com/weather-song/68123/")
    return weather_song.status_code==200