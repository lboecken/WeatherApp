import os
from twilio.rest import Client
from collections import OrderedDict
from ClassManager import class_manager

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


class WeatherSMSPreparerAndSender:

    def __init__(self):

    def determine_what_weather_information_template_to_use(self, next_message_to_send):
        if next_message_to_send[5] == "Daily"


    @staticmethod
    def daily(message_info, weather_info):
        client.messages.create(
            from_='14704358197',
            body=
            f'''Hello {message_info["Name"]}, The weather at {message_info["Location_Name"]} is the following for today:
    MORNING: {weather_info["morn"]}
    DAY: {weather_info["day"]}
    EVENING {weather_info["eve"]}
    NIGHT: {weather_info["night"]}
    HIGH: {weather_info["high"]}
    LOW: {weather_info["low"]}
    FORECAST: {weather_info["description"]}
            ''',
            to=message_info["Phone_Number"]
        )

    @staticmethod
    def weekly(message_info, weather_info=OrderedDict):
        for key in weather_info.keys():
            client.messages.create(
                from_='14704358197',
                body=
                f'''Hello {message_info["Name"]}, The weather at {message_info["Location_Name"]} is the following for {weather_info[key]["day of week"]}:
    MORNING: {weather_info[key]["morn"]}
    DAY: {weather_info[key]["day"]}
    EVENING {weather_info[key]["eve"]}
    NIGHT: {weather_info[key]["night"]}
    HIGH: {weather_info[key]["high"]}
    LOW: {weather_info[key]["low"]}
    FORECAST: {weather_info[key]["description"]}
                        ''',
                to=message_info["Phone_Number"]
            )
