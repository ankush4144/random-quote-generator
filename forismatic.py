#random quote generator


import requests
import json
 
url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
 
resp = requests.get(url=url)
data = json.loads(resp.text)



print(data['quoteText'] + '.\n' + data['quoteAuthor'])
