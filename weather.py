import requests


class Weather:
    api_key = "6fc81eb8419eb5f802d034d404388e79"

    def __init__(self, name):
        self.latitude = name.coordinates["latitude"]
        self.longitude = name.coordinates["longitude"]
        self.weather_api_json = None
        self.sky = None
        self.temperature = None
        self.feels_like = None
        self.minimum_temperature = None
        self.maximum_temperature = None
        self.current_humidity = None

    # noinspection SpellCheckingInspection
    def openweather_api_pull(self):
        self.weather_api_json = requests.get(
         f"http://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units=imperial").json()
        return self.current_weather_update()

    def current_weather_update(self):
        self.sky = self.weather_api_json["weather"][0]["description"]
        self.temperature = self.weather_api_json["main"]["temp"]
        self.feels_like = self.weather_api_json["main"]["feels_like"]
        self.minimum_temperature = self.weather_api_json["main"]["temp_min"]
        self.maximum_temperature = self.weather_api_json["main"]["temp_max"]
        self.current_humidity = self.weather_api_json["main"]["humidity"]
