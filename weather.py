import requests
from geopy.geocoders import ArcGIS
from twilio.rest import Client
import pandas

# PROJECT SCOPE
# ENTER ADDRESS, PULL COORDINATES --> GEOPY
# PULL WEATHER.COM API
# FORMAT INTO MY WEBSITE
# TEXT DATA TO A PHONE -> TWILIO
# AUTOMATE TO RUN ON A DAILY BASIS -> Raspberry Pi
# TODO Add CSV File to store user data.
class Dataframe:
    def __init__(self):
        self.list_of_people = pandas.DataFrame()






class Individual:
    def __init__(self, name):
        self.address = None
        self.coordinates_from_address = None
        self.name = name

    def GetAddress(self):
        if self.address == None:
            self.address = input("Please enter your city, state, and zip code: ")
        else:
            pass

    def AddressToCoordinates(self, address):
        if self.coordinates_from_address == None:
            self.coordinates_from_address = ArcGIS()
            self.coordinates_from_address = {"latitude": self.coordinates_from_address.geocode(address).latitude,
                                             "longitude": self.coordinates_from_address.geocode(address).longitude}

    def WriteToCSV(self, address, coordinates=):




# Twilio account authentication.
account_sid = "AC39bcb788f57cd6240b58284c89470e2e"
auth_token = "12adef0e15473b80810c34c15c011d66"
client = Client(account_sid, auth_token)


def get_address():
    address = input("Please enter your city, state and zip code: ")
    return address


# turns addresss into latitude & longitude stored in dict.
def address_to_coordinates(address):
    coordinates_object = ArcGIS()
    coordinates_dict = {"latitude": coordinates_object.geocode(address).latitude,
                        "longitude": coordinates_object.geocode(address).longitude}
    return coordinates_dict


# could add a para arg for determining units.
def openweather_api_pull(coordinates, ):
    lat = coordinates["latitude"]
    lon = coordinates["longitude"]
    api_key = "6fc81eb8419eb5f802d034d404388e79"
    weather_api_json = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial").json()
    return weather_api_json


address = get_address()
coordinates = address_to_coordinates(address)
weather_api_json = openweather_api_pull(coordinates)

message = client.messages \
    .create(
    body=f"The temperature today is {weather_api_json['main']['temp']} degrees Fahrenheit in {address}. Enjoy! TEST3",
    from_="+14704358197",
    to="+14045094520"
)
