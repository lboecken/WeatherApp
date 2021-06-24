import sqlite3
import time


class DatabaseManager:

    def __init__(self):
        pass

    def add_user(self, user_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "INSERT INTO users ('NAME', 'PHONENUMBER', 'TIMEZONE') values (?, ?, ?)",
            user_info)
        connection_to_db.commit()
        connection_to_db.close()

    def add_new_location_for_user(self, location_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "INSERT INTO locations "
            "('USER_ID', 'ADDRESS_NAME', 'ADDRESS', 'LATITUDE', 'LONGITUDE') "
            "values (?, ?, ?, ?, ?)", location_info)
        connection_to_db.commit()
        connection_to_db.close()

    def add_new_message_for_user(self, message_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "INSERT INTO message"
            "('USER_ID', 'LOCATION_ID', 'WEEKDAY', 'TIME_OF_DAY', 'REPEAT_FACTOR', 'TIME_OF_NEXT_MESSAGE') "
            "values (?, ?, ?, ?, ?, ?)", message_info)
        connection_to_db.commit()
        connection_to_db.close()

    def delete_location_for_user(self, name_of_location):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "DELETE FROM locations WHERE ADDRESS_NAME = ?", name_of_location)
        connection_to_db.commit()
        connection_to_db.close()

    def delete_message_for_user(self, nickname_of_message):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "DELETE FROM message WHERE NICKNAME = ?", nickname_of_message)
        connection_to_db.commit()
        connection_to_db.close()
        pass

    def grab_next_messages_to_send(self):
        current_time_in_seconds_since_epoch = int(time.time())
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        next_messages_to_send = list(connection_cursor.execute(
            "SELECT * FROM message WHERE TIME_OF_NEXT_MESSAGE < ?", (str({current_time_in_seconds_since_epoch + 59}),)))
        if not next_messages_to_send:
            pass
        else:
            for x in next_messages_to_send:
                self.send_next_message_info_to_twilio(x)
                self.update_timeofnextmessage_in_Database_for_last_sent_message(x)
            connection_to_db.close()

    def send_next_message_info_to_twilio(self, message_info):

        pass

    def update_timeofnextmessage_in_Database_for_last_sent_message(self, message_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        if message_info[5] == 0:
            connection_cursor.execute('DELETE FROM message WHERE MESSAGE_ID = ?', (message_info[0],))
            connection_to_db.commit()
            connection_to_db.close()
        else:
            pass





