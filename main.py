from weather import Weather
from sqldb import DatabaseManager
import twilio_service
from twilio_service import WeatherSMS
import pprint


def main():
    message_info = (1,1,1,1,0,1624492299)
    x = 0
    db = DatabaseManager()
    # while x < 7:
    #     db.add_new_message_for_user(message_info)
    #     x += 1
    db.grab_next_messages_to_send()






if __name__ == "__main__":
    main()



