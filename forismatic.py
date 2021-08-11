#random quote generator

from datetime import datetime
import json
import logging
import requests


console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('[%(asctime)s]-[%(levelname)s][%(threadName)s]:%(message)s'))
# Create and configure logger
logging.basicConfig(filename=f"quote_generator-{str(datetime.now())}.log",
                    format='[%(asctime)s]-[%(levelname)s][%(threadName)s]:%(message)s',
                    filemode='w',
                    level=logging.DEBUG)
logging.getLogger().addHandler(console)
logger = logging.getLogger()

 
url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en'


logger.info(f"Sending GET request to API - {url}")
resp = requests.get(url=url)
logger.debug(f"STATUS CODE - {resp.status_code}")
logger.debug(f"API RESPONSE - {resp.content}")


if resp.status_code == 200:
    logger.info("API response request successful with Status Code - 200")
    logger.info("Attempting to render data received from API response to JSON")
    # quote response received from API
    quote = str(resp.content)
else:
    raise Exception("Failed to fetch data from API")

logger.info(f"Quote received from API \n{quote}")

filename = "quote.txt"
logger.debug("Writing the quote to a file")
try:
    with open(filename, "w") as file:
        file.write(quote)
except Exception as err:
    raise Exception(f"Failed to write the quote to file due to err - {str(err)}")


logger.info(f"Successfully wrote quote '{quote}' to file '{filename}'")

