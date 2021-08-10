#random quote generator


import requests
import json
 
url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
 
resp = requests.get(url=url)

if resp.status_code == 200:
    print("API RESPONSE", resp.content)
    data = resp.json()
else:
    raise Exception("Failed to fetch data from API")

print(data['quoteText'] + '.\n' + data['quoteAuthor'])
