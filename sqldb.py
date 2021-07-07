import sqlite3
import ClassManager
import time


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
        connection_to_db = sqlite3.connect("test.db")
        cursor = connection_to_db.cursor()
        cursor.execute(
            #this needs to be altered to function based of the logic of days of the week & time)
            "SELECT * FROM messages INNER JOIN USERS ON MESSAGES.USER_ID = USERS.USER_ID")
        next_messages_to_send = cursor.fetchall()
        if not next_messages_to_send:
            pass
        else:
            for x in next_messages_to_send:
                ClassManager.class_manager.weatherapimanager.openweather_api_pull(x)
                ClassManager.class_manager.twilioservicemanager.determine_what_weather_information_template_to_use(x)
            connection_to_db.close()






