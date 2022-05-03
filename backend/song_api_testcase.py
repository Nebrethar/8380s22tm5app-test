import requests

def test_random_song():
    random_song = requests.get("https://8380s22tm5app.com/random-song/")
    return random_song.status_code==200

def test_weather_song():
    weather_song = requests.get("https://8380s22tm5app.com/weather-song/68123/")
    return weather_song.status_code==200

def test_youtube():
    weather_song = requests.get("https://8380s22tm5app.com/get-youtube/artist/song/")
    return weather_song.status_code==200

def test_playlist():
    weather_song = requests.get("https://8380s22tm5app.com/get-playlists/")
    return weather_song.status_code==200