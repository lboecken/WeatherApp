import requests
import time
import os
from collections import OrderedDict


class WeatherInformation:
    api_key = os.environ['WeatherApiKey']

    def __init__(self):
        self.weather_api_json = None
        self.daily = {}

    # noinspection SpellCheckingInspection
    def openweather_api_pull(self, message_info_from_db):
        self.weather_api_json = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={message_info_from_db[3]}&lon={message_info_from_db[4]}&exclude=&appid={self.api_key}&units=imperial").json()
        return self.prepare_and_organize_weather_information()

    def prepare_and_organize_weather_information(self):
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
        except KeyError:
            return "NA"

