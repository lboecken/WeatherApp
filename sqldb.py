import sqlite3


class DatabaseManager:

    def __init__(self):
        pass

    def add_user(self, user_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute("INSERT INTO main ('NAME', 'PHONENUMBER') values (?, ?)", user_info)
        connection_to_db.commit()

    def add_new_location_for_user(self, location_info):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "INSERT INTO locations ('USER_ID', 'ADDRESS_NAME', 'ADDRESS', 'LATITUDE', 'LONGITUDE') "
            "values (?, ?, ?, ?, ?)", location_info)
        connection_to_db.commit()

    def add_new_message_for_user(self):
        connection_to_db = sqlite3.connect("test.db")
        connection_cursor = connection_to_db.cursor()
        connection_cursor.execute(
            "INSERT INTO locations ('USER_ID', 'ADDRESS_NAME', 'ADDRESS', 'LATITUDE', 'LONGITUDE') values (?, ?, ?, ?, ?)",
            location_info)
        connection_to_db.commit()

    def delete_location_for_user(self):
        pass

    def delete_message_for_user(self):
        pass

    def check_for_next_message_to_send(self): #will be run by Heroku Chron job every 1/5 minutes
        pass

    def pass_message_data_to_twilio_for_sending(self):
        pass