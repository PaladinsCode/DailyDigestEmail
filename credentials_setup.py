import json
file = open("api_credentials.json")
setup_params = json.load(file)


# Set up Parameters import
OPEN_WEATHER_API_KEY   = setup_params["open weather api key"]
TWITTER_API_KEY        = setup_params["twitter api key"]
TWITTER_API_SECRET_KEY = setup_params["twitter api secret key"]
