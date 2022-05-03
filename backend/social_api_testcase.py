import requests

def test_twitter():
    random_song = requests.get("https://8380s22tm5app.com/twitter-post/")
    return random_song.status_code==200

def test_facebook():
    weather_song = requests.get("https://8380s22tm5app.com/facebook-post/")
    return weather_song.status_code==200