import requests
import pprint
import datetime

API_KEY=config.SKYSCANNER_TOKEN


def get_polling_url(originplace,destinationplace,outbounddate):

    headers= { "Content-Type": "application/x-www-form-urlencoded",
               "Accept": "application/json"}

    params={
      "country":"UK",
      "currency":"GBP",
      "locale":"en-GB",
      "originplace":originplace,
      "destinationplace":destinationplace,
      "outbounddate":outbounddate,
      "adults":1,
      "locationschema":"Sky"
    }

    url="http://partners.api.skyscanner.net/apiservices/pricing/v1.0?apiKey=%s"%API_KEY

    result = requests.post(url,headers=headers,data=params)
    return result.headers['location']


def get_top_results(nresults,pollingUrl):
    result= requests.get("{0}?apiKey={1}&pagesize={2}".format(pollingUrl,API_KEY,nresults))
    open('flights.json','w').write(result.text.encode('utf8'))
    data = result.json()
    agents = data['Agents']
    flights = data['Itineraries'][:nresults]
    results=[]
    for flight in flights:
        first_price= flight['PricingOptions'][0]
        agent_name= [ a["Name"] for a in agents if a['Id']== first_price['Agents'][0]][0]
        results.append((agent_name,first_price['Price']))

    return(results)

def get_top_place(place_string):
    url="http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/GB/GBP/en-GB?query={0}&apiKey={1}".format(place_string,API_KEY)
    result = requests.get(url)
    place_id = result.json()['Places'][0]['PlaceId']
    return place_id


def flight_prices(origin_string,destination_string,date):
    originplace = get_top_place(origin_string)
    destinationplace = get_top_place(destination_string)
    outbounddate = date.strftime("%Y-%m-%d")
    polling_url = get_polling_url(originplace,destinationplace,outbounddate)
    return get_top_results(3,polling_url)

