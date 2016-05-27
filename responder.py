import requests
import config
import pprint
import datetime
from skyscanner import flight_prices

def get_wit_response(text):
    TOKEN=config.WIT_TOKEN
    WIT_API='https://api.wit.ai/message'
    payload= {"v":"20160527","q":text}
    headers = {"Authorization":"Bearer %s"%TOKEN}
    result = requests.get(WIT_API,headers=headers,params=payload)
    return(result.json())


def generate_response(text):
    try: 
        wit_response = get_wit_response(text)
        date_str = wit_response["entities"]["datetime"][0]["value"].split('T')[0]
        date=datetime.datetime.strptime(date_str,"%Y-%m-%d")
        origin_str = wit_response["entities"]["from"][0]["value"]
        destination_str = wit_response["entities"]["to"][0]["value"]

        flights = flight_prices (origin_str,destination_str,date)
        return str(flights)
    except:
        return "Sorry! I'm not sure how to help you"




