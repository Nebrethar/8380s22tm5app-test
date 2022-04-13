import requests

def test_fb_login():
    facebook = requests.get("https://8380s22tm5app.com/facebook-post/")
    return facebook.status_code==200

def test_twitter_login():
    twitter = requests.get("https://8380s22tm5app.com/weather-song/68123/")
    return twitter.status_code==200