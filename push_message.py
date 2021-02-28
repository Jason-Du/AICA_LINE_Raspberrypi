
import requests
data = {
    "name": "Jason",
    "photo": "ON"
}
print(data.keys())
# "message from desktop"
#r = requests.get('https://526d2abb9346.ngrok.io/foodlinebot/callback', params=data)
r = requests.get('https://72dc5ebca7fa.ngrok.io/callback', params=data)
r.close()