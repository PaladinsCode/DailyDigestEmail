from urllib import request
import json
import datetime

def get_weather_forecast(coords={'lat': 38.9637, 'lon': 35.2433}): # default location at Cape Canaveral, FL
    try: # retrieve forecast for specified coordinates
        api_key = '73031409e60a0b4de8e37fe0990a5a6b' # OpenWeatherMap API key
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        print("This is the url: ", url)
        data = json.load(request.urlopen(url))
        print("This is the data: ", data)

        with open("OpenWeatherApiCall.json", "w") as write_file:
            json.dump(data, write_file, indent=4, sort_keys=True, separators=(',', ': '))
        print("Done writing JSON data into file without Pretty Printing it")

        forecast = {'city'   : data['city']['name'], # city name
                    'country': data['city']['country'], # country name
                    'periods': list()} # list to hold forecast data for future periods

        for period in data['list'][0:9]: # populate list with next 9 forecast periods 
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
        
        return forecast

    except Exception as e:
        print(e)   

##### test get_weather_forecast() #####
print('\nTesting weather forecast retrieval...')

forecast = get_weather_forecast() # get forecast for default location
if forecast:
    print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
    for period in forecast['periods']:
        print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

# austin = {'lat': 30.2748,'lon': -97.7404} # coordinates for Texas State Capitol
# forecast = get_weather_forecast(coords = austin) # get Austin, TX forecast
# if forecast:
#     print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
#     for period in forecast['periods']:
#         print(f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}')

# invalid = {'lat': 1234.5678 ,'lon': 1234.5678} # invalid coordinates
# forecast = get_weather_forecast(coords = invalid) # get forecast for invalid location
# if forecast is None:
#     print('Weather forecast for invalid coordinates returned None')