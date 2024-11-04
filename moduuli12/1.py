import http.client
import json

def fetch_chuck_norris_joke():
    conn = http.client.HTTPSConnection("api.chucknorris.io")
    conn.request("GET", "/jokes/random")
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read()
        joke_data = json.loads(data)
        joke = joke_data['value']
        print("Chuck Norris Joke:")
        print(joke)
    else:
        print("Failed to retrieve joke. Status code:", response.status)
    
    conn.close()

fetch_chuck_norris_joke()
