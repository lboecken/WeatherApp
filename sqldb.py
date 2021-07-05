import sqlite3
import time
from ClassManager import class_manager


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

    def add_new_message_for_user(self, message_info):
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            "INSERT INTO message"
            "('USER_ID', 'ADDRESS', 'LATITUDE', 'LONGITUDE', 'WEATHER_INFORMATION', "
            "'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'TIME_OF_DAY') "
            "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", message_info)
        connection_to_db.commit()
        connection_to_db.close()

    def delete_message_for_user(self, message_id):
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            "DELETE FROM messages WHERE MESSAGE_ID = ?", message_id)
        connection_to_db.commit()
        connection_to_db.close()
        pass

    def grab_next_messages_to_send(self):
        current_time_in_seconds_since_epoch = int(time.time())
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            #this needs to be altered to function based of the logic of days of the week & time)
            "SELECT * FROM message WHERE TIME_OF_NEXT_MESSAGE < ?", (str({current_time_in_seconds_since_epoch + 59}),))
        next_messages_to_send = cursor.fetchall()
        if not next_messages_to_send:
            pass
        else:
            for x in next_messages_to_send:
                class_manager.weatherapimanager.openweather_api_pull(x)
                class_manager.twilioservicemanager.
            connection_to_db.close()






