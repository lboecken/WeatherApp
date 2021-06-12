from weather import Weather
from sqldb import DatabaseManager
import twilio_service
from twilio_service import WeatherSMS
import pprint


def main():
    user_info = {"Name": "Lennart", "Location_Name": "Home", "Phone_Number": "14045094520"}
    weather = Weather()
    weather.openweather_api_pull(34.23, -80.23)
    WeatherSMS.weekly(user_info, weather.daily)


if __name__ == "__main__":
    main()


print('Hello World')
