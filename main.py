import os
from dotenv import load_dotenv
import requests

# for details see https://openweathermap.org/current
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?" 

# default query
CITY = "Bremen"

def report_temp(query, key):
    # construct request url
    URL = f"{BASE_URL}q={query}&appid={key}"

    # query api
    response = requests.get(URL)

    # if failed indicate http error status to caller 
    if response.status_code != 200:
        raise Exception(f"Error in the HTTP request:{response.status_code}")

    # parse response from json
    data = response.json()

    # find temperature in returned data set
    # there are a lot more interesting data points in here like 
    # humidity, pressure etc in data['main'] 
    # and a description of the weather in data['report'] 
    # for details see https://openweathermap.org/current#parameter
    main = data['main']
    temperature = main['temp']

    # prettyprint result
    return f"Current temperature in {query} is {k_to_c(temperature):.2f}°C"

# convert temperature in kelvin to celsius 
def k_to_c(temp):
    return temp - 273.15

if __name__ == "__main__":
    # load environment from .env
    load_dotenv()
    QUERY = os.getenv('QUERY')
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

    # fail if api key is missing
    if OPENWEATHER_API_KEY == None:
        raise Exception("Please define OPENWEATHER_API_KEY in your .env file!")
    
    # use defualt query if none is defined in .env 
    if QUERY == None: 
        QUERY = CITY
    try:
        print(report_temp(QUERY, OPENWEATHER_API_KEY))
    except Exception as error:
        print(error)
        exit(-1)
    exit(0)