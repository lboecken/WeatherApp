import requests
import time
import os
from collections import OrderedDict
from geopy import ArcGIS


def address_to_coordinates_converter(address):
    converter = ArcGIS()
    coordinates = {'latitude': converter.geocode(address).latitude, 'longitude': converter.geocode(address).longitude}
    return coordinates


class WeatherInformation:
    api_key = os.environ['WeatherApiKey']

    def __init__(self):
        self.weather_api_json = None
        self.seven_day_weather_information = {}
        self.todays_weather_information = {}

    def openweather_api_pull(self, message_info_from_db):
        self.weather_api_json = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={message_info_from_db[4]}&lon={message_info_from_db[5]}&exclude=&appid={self.api_key}&units=imperial").json()
        return self.prepare_seven_day_weather_information(), self.prepare_today_weather_information()

    def prepare_seven_day_weather_information(self):
        for i in range(0, 8):
            self.seven_day_weather_information.update(
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
                      'rain': self.check_if_rain_information_is_available(i),
                      'day of week': self.determine_day_of_week(i)
                      }
                 })
            )

    def prepare_today_weather_information(self):
        self.todays_weather_information = {
            'morn': round(self.weather_api_json["daily"][0]["temp"]["morn"]),
            'day': round(self.weather_api_json["daily"][0]["temp"]["day"]),
            'eve': round(self.weather_api_json["daily"][0]["temp"]["eve"]),
            'night': round(self.weather_api_json["daily"][0]["temp"]["night"]),
            'high': round(self.weather_api_json["daily"][0]["temp"]["max"]),
            'low': round(self.weather_api_json["daily"][0]["temp"]["min"]),
            'description': self.weather_api_json["daily"][0]["weather"][0]["description"],
            'humidity': self.weather_api_json["daily"][0]["humidity"],
            'uvi': self.weather_api_json["daily"][0]["uvi"],
            'rain': self.check_if_rain_information_is_available(0)
                      }

    def determine_date(self, i):
        date_information = time.localtime(self.weather_api_json["daily"][i]["dt"])
        return time.strftime('%Y%m%d', date_information)

    def determine_day_of_week(self, i):
        date_information = time.localtime(self.weather_api_json["daily"][i]["dt"])
        return time.strftime('%A, %B %d', date_information)

    def check_if_rain_information_is_available(self, i):
        try:
            self.seven_day_weather_information.update(
                {self.determine_date(i):
                     {"rain": self.weather_api_json["daily"][i]["rain"]
                      }
                 }
            )
        except KeyError:
            return "NA"

