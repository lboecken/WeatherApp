import ClassManager as CM
import datetime
from weather_and_geocoordinates import address_to_coordinates_converter
import psycopg2
import os

database_url = os.environ['DATABASE_URL']

class DatabaseManager:

    def __init__(self):
        pass


    def add_user(self, user_info):
        connection_to_db = psycopg2.connect(database_url)
        connection_cursor = connection_to_db.cursor()
        sql = '''INSERT INTO USERS 
        (NAME, PHONE_NUMBER, TIMEZONE) 
        VALUES (%s, %s, %s)'''
        connection_cursor.execute(sql, user_info)
        connection_to_db.commit()
        connection_to_db.close()

    def prepare_data_for_insert_into_sql_db(self,
                                            user_id: int,
                                            address: str,
                                            address_name:str,
                                            coordinates: dict,
                                            weather_info: str,
                                            days: tuple,
                                            time_of_day: str):
        data = (user_id,address,address_name, coordinates['latitude'], coordinates['longitude'], weather_info, days[0],
                days[1], days[2], days[3], days[4], days[5], days[6], time_of_day)
        return self.add_new_message_for_user_to_db(data)

    def add_new_message_for_user_to_db(self, data):
        connection_to_db = psycopg2.connect(database_url)
        cursor = connection_to_db.cursor()
        sql = '''INSERT INTO messages
            (USER_ID, ADDRESS, ADDRESS_NAME, LATITUDE, LONGITUDE, WEATHER_INFORMATION, 
            MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, TIME_OF_DAY) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, data)
        connection_to_db.commit()
        connection_to_db.close()

    def delete_message_for_user_from_db(self, message_id):
        connection_to_db = psycopg2.connect(database_url)
        cursor = connection_to_db.cursor()
        cursor.execute(
            "DELETE FROM messages WHERE MESSAGE_ID = ?", message_id)
        connection_to_db.commit()
        connection_to_db.close()
        pass

    def lookup_time_and_date_to_determine_next_messages_to_send_out(self):
        x = datetime.datetime.now()
        time_for_next_messages = x.strftime("%H:%M")
        day_for_next_messages = x.strftime('%A').upper()
        return self.grab_next_messages_to_send_from_db_and_handoff(time_for_next_messages, day_for_next_messages)

    def grab_next_messages_to_send_from_db_and_handoff(self, time_for_next_messages, day_for_next_messages):
        connection_to_db = psycopg2.connect(database_url)
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






