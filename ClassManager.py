import sqldb
import weather
import twilio_service


class ClassManager:

    def __init__(self):
        self.databasemanager = sqldb.DatabaseManager()
        self.weatherapimanager = weather.WeatherInformation()
        self.twilioservicemanager = twilio_service.WeatherSMSPreparerAndSender()


class_manager = ClassManager()