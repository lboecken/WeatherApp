import sqlite3
import ClassManager as CM
import datetime
from weather_and_geocoordinates import address_to_coordinates_converter


class DatabaseManager:

    def __init__(self):
        pass

    def add_user(self, user_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "INSERT INTO users ('NAME', 'PHONE_NUMBER', 'TIMEZONE') values (?, ?, ?)",
            user_info)
        connection_to_db.commit()
        connection_to_db.close()

    def add_new_message_for_user_to_db(self, message_info):
        #coordinates = address_to_coordinates_converter(message_info())
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            "INSERT INTO message"
            "('USER_ID', 'ADDRESS', 'LATITUDE', 'LONGITUDE', 'WEATHER_INFORMATION', "
            "'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'TIME_OF_DAY') "
            "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", message_info)
        connection_to_db.commit()
        connection_to_db.close()

    def delete_message_for_user_from_db(self, message_id):
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            "DELETE FROM messages WHERE MESSAGE_ID = ?", message_id)
        connection_to_db.commit()
        connection_to_db.close()
        pass

    def determine_what_messages_need_to_be_pulled_next(self):
        x = datetime.datetime.now()
        time_for_next_messages = x.strftime("%H:%M")
        day_for_next_messages = x.strftime('%A').upper()
        return self.grab_next_messages_to_send_from_db_and_handoff(time_for_next_messages, day_for_next_messages)

    def grab_next_messages_to_send_from_db_and_handoff(self, time_for_next_messages, day_for_next_messages):
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            f"SELECT * FROM messages INNER JOIN USERS ON MESSAGES.USER_ID = USERS.USER_ID WHERE TIME_OF_DAY = ? AND {day_for_next_messages} = 1", (time_for_next_messages, ))
        #No the above is not recommended but no user has access to this function to inject something & it works. I'll get better at this later.
        next_messages_to_send = cursor.fetchall()
        if not next_messages_to_send:
            pass
        else:
            for x in next_messages_to_send:
                CM.class_manager.weatherapimanager.openweather_api_pull(x)
                CM.class_manager.twilioservicemanager.determine_what_weather_information_template_to_use(x)
            connection_to_db.close()






