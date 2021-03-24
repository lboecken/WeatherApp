import requests
import time


class Weather:
    api_key = "6fc81eb8419eb5f802d034d404388e79"

    def __init__(self, name):
        self.latitude = name.coordinates["latitude"]
        self.longitude = name.coordinates["longitude"]
        self.weather_api_json = None
        self.current = {}
        self.hourly = {}
        self.daily = {}
        self.openweather_api_pull()

    # noinspection SpellCheckingInspection
    def openweather_api_pull(self):
        self.weather_api_json = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&exclude=&appid={self.api_key}&units=imperial").json()
        return self.current_weather_update(), self.hourly_weather_update(), self.daily_weather_update()

    def current_weather_update(self):
        self.current = {"current_temp": round(self.weather_api_json["current"]["temp"]),
                        "feels_like": round(self.weather_api_json["current"]["feels_like"]),
                        "description": self.weather_api_json["current"]["weather"][0]["description"],
                        "humidity": str(self.weather_api_json["current"]["humidity"]) + "%",
                        "sunrise": time.localtime(self.weather_api_json["current"]["sunrise"]),
                        "sunset": time.localtime(self.weather_api_json["current"]["sunset"])}

    def hourly_weather_update(self):
        for i in range(0, 48):
            self.hourly.update(
                {i:
                     {"current_temp": round(self.weather_api_json["hourly"][i]["temp"]),
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
                {self.determine_date_and_day(i):
                     {'morn': round(self.weather_api_json["daily"][i]["temp"]["morn"]),
                      'day': round(self.weather_api_json["daily"][i]["temp"]["day"]),
                      'eve': round(self.weather_api_json["daily"][i]["temp"]["eve"]),
                      'night': round(self.weather_api_json["daily"][i]["temp"]["night"]),
                      'max': round(self.weather_api_json["daily"][i]["temp"]["max"]),
                      'min': round(self.weather_api_json["daily"][i]["temp"]["min"]),
                      'description': self.weather_api_json["daily"][i]["weather"][0]["description"],
                      'humidity': self.weather_api_json["daily"][i]["humidity"],
                      'uvi': self.weather_api_json["daily"][i]["uvi"],
                      'rain': self.check_if_rain_available(i)
                      }
                 }
            )

    def determine_date_and_day(self, i):
        date_information = time.localtime(self.weather_api_json["daily"][i]["dt"])
        return time.strftime('%c', date_information)

    def check_if_rain_available(self, i):
        try:
            self.daily.update(
                {self.determine_date_and_day(i):
                     {"rain": self.weather_api_json["daily"][i]["rain"]
                      }
                 }
            )
        except:
            KeyError
            return "NA"

