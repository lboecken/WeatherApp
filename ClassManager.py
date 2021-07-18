import sqldb
import weather_and_geocoordinates
import twilio_service


class ClassManager:

    def __init__(self):
        self.databasemanager = sqldb.DatabaseManager()
        self.weatherapimanager = weather_and_geocoordinates.WeatherInformation()
        self.twilioservicemanager = twilio_service.WeatherSMSPreparerAndSender()


class_manager = ClassManager()