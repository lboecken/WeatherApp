import requests
import time
import os
from collections import OrderedDict


class Weather:
    api_key = os.environ['WeatherApiKey']

    def __init__(self):
        self.weather_api_json = None
        self.current = {}
        self.hourly = {}
        self.daily = {}

    # noinspection SpellCheckingInspection
    def openweather_api_pull(self, latitude, longitude):
        self.weather_api_json = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=&appid={self.api_key}&units=imperial").json()
        return self.current_weather_update(), self.hourly_weather_update(), self.daily_weather_update()

    def current_weather_update(self):
        self.current = {"current_temp": round(self.weather_api_json["current"]["temp"]),
                        "feels_like": round(self.weather_api_json["current"]["feels_like"]),
                        "description": self.weather_api_json["current"]["weather"][0]["description"],
                        "humidity": str(self.weather_api_json["current"]["humidity"]) + "%",
                        "sunrise": (self.weather_api_json["current"]["sunrise"]),
                        "sunset": (self.weather_api_json["current"]["sunset"])}

    def hourly_weather_update(self):
        for i in range(0, 48):
            self.hourly.update(
                {i:
                     {'current_temp': round(self.weather_api_json["hourly"][i]["temp"]),
                      "feels_like": round(self.weather_api_json["hourly"][i]["feels_like"]),
                      "description": self.weather_api_json["hourly"][i]["weather"][0]["description"],
                      "humidity": str(self.weather_api_json["hourly"][i]["humidity"]) + "%",
                      "uvi": self.weather_api_json["hourly"][i]["uvi"]
                      }
                 }
            )

    def daily_weather_update(self):
        for i in range(0, 8):
            self.daily.update(
                OrderedDict({self.determine_date(i):
                     {'morn': round(self.weather_api_json["daily"][i]["temp"]["morn"]),
                      'day': round(self.weather_api_json["daily"][i]["temp"]["day"]),
                      'eve': round(self.weather_api_json["daily"][i]["temp"]["eve"]),
                      'night': round(self.weather_api_json["daily"][i]["temp"]["night"]),
                      'high': round(self.weather_api_json["daily"][i]["temp"]["max"]),
                      'low': round(self.weather_api_json["daily"][i]["temp"]["min"]),
                      'description': self.weather_api_json["daily"][i]["weather"][0]["description"],
                      'humidity': self.weather_api_json["daily"][i]["humidity"],
                      'uvi': self.weather_api_json["daily"][i]["uvi"],
                      'rain': self.check_if_rain_available(i),
                      'day of week': self.determine_day_of_week(i)
                      }
                 })
            )

    def determine_date(self, i):
        date_information = time.localtime(self.weather_api_json["daily"][i]["dt"])
        return time.strftime('%Y%m%d', date_information)

    def determine_day_of_week(self, i):
        date_information = time.localtime(self.weather_api_json["daily"][i]["dt"])
        return time.strftime('%A, %B %d', date_information)

    def check_if_rain_available(self, i):
        try:
            self.daily.update(
                {self.determine_date(i):
                     {"rain": self.weather_api_json["daily"][i]["rain"]
                      }
                 }
            )
        except:
            KeyError
            return "NA"

