#random quote generator


import requests
import json
 
url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
 
resp = requests.get(url=url)

if resp.status_code == 200:
    print("API RESPONSE", resp.content)
    try:
        try:
            data = resp.json()
        except json.decoder.JSONDecodeError:
            data = eval(resp.content)
    except:
        raise Exception("Failed to decode the response received from API")
else:
    raise Exception("Failed to fetch data from API")

qoute = data['quoteText'] + '.\n' + data['quoteAuthor']

print(quote)

filename = "quote.txt"

with open(filename, "w") as file:
    file.write(quote)

