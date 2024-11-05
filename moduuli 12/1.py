import http.client
import json

def fetch_chuck_norris_joke():
    conn = http.client.HTTPSConnection("api.chucknorris.io")
    
    try:
        conn.request("GET", "/jokes/random")
        response = conn.getresponse()
        
        if response.status == 200:
            data = response.read()
            joke_data = json.loads(data)
            joke = joke_data['value']
            
            print("Chuck Norris Joke:")
            print(joke)
        
        else:
            print(f"Failed to fetch joke, status code: {response.status}")
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        conn.close()

fetch_chuck_norris_joke()
