import os
from twilio.rest import Client
from collections import OrderedDict
import ClassManager as CM

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
outbound_phone_number = os.environ['OUTBOUND_NUMBER']
client = Client(account_sid, auth_token)


class WeatherSMSPreparerAndSender:

    def determine_what_weather_information_template_to_use(self, next_message_to_send):
        if next_message_to_send[6] == "DAILY":
            return self.send_out_daily_weather_report(next_message_to_send, CM.class_manager.weatherapimanager.todays_weather_information)
        elif next_message_to_send[6] == "7_DAY_REPORT":
            return self.send_out_seven_day_weather_report(next_message_to_send, CM.class_manager.weatherapimanager.seven_day_weather_information)

    @staticmethod
    def send_out_daily_weather_report(message_info, weather_info):
        client.messages.create(
            from_= outbound_phone_number,
            body=
            f'''Hello {message_info[16]}, The weather at {message_info[3]} is the following for today:
    MORNING: {weather_info["morn"]}
    DAY: {weather_info["day"]}
    EVENING {weather_info["eve"]}
    NIGHT: {weather_info["night"]}
    HIGH: {weather_info["high"]}
    LOW: {weather_info["low"]}
    FORECAST: {weather_info["description"]}
            ''',
            to=message_info[17]
        )

    @staticmethod
    def send_out_seven_day_weather_report(message_info, weather_info=OrderedDict):
        for key in weather_info.keys():
            client.messages.create(
                from_= outbound_phone_number,
                body=
                f'''Hello {message_info[16]}, The weather at {message_info[3]} is the following for {weather_info[key]["day of week"]}:
    MORNING: {weather_info[key]["morn"]}
    DAY: {weather_info[key]["day"]}
    EVENING {weather_info[key]["eve"]}
    NIGHT: {weather_info[key]["night"]}
    HIGH: {weather_info[key]["high"]}
    LOW: {weather_info[key]["low"]}
    FORECAST: {weather_info[key]["description"]}
                        ''',
                to=message_info[17]
            )

