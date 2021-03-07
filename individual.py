from geopy import ArcGIS
import pandas as pd
import data_managment


class Individual:
    def __init__(self, name, phone_number=0):
        self.name = name
        self.address = ""
        self.coordinates = {}
        self.phone_number = phone_number
        self.info_for_dataframe = pd.DataFrame()
        self.get_address()
        self.convert_address_to_coordinates(self.address)


    def get_address(self):
        if self.address == "":
            self.address = input("Please enter your city, state, and zip code: ")
        else:
            pass

    def convert_address_to_coordinates(self, address):
        if self.coordinates == {}:
            self.coordinates = ArcGIS()
            self.coordinates = {"latitude": self.coordinates.geocode(address).latitude,
                                "longitude": self.coordinates.geocode(address).longitude}
        else:
            pass

    def get_info_for_dataframe(self):
        if self.info_for_dataframe == pd.DataFrame():
            self.info_for_dataframe = pd.DataFrame([[self.name,
                                                     self.address,
                                                     self.coordinates["latitude"],
                                                     self.coordinates["longitude"]]],
                                                   columns=data_managment.column_names)
        else:
            pass

