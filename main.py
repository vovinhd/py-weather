import os
from dotenv import load_dotenv
import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Bremen"

def main():
    load_dotenv()
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    if OPENWEATHER_API_KEY == None:
        print("Please define OPENWEATHER_API_KEY in your .env file!")
        exit(-1)
    URL = BASE_URL + "q=" + CITY + "&appid=" + OPENWEATHER_API_KEY
    response = requests.get(URL)
    if response.status_code != 200:
        print("Error in the HTTP request")
    data = response.json()
    main = data['main']
    temperature = main['temp']
    print(f"Temperature: {k_to_c(temperature)}")
    exit(0)

def k_to_c(temp):
    return temp - 273.15

if __name__ == "__main__":
    main()