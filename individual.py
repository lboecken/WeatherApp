from geopy import ArcGIS
import pandas


class Individual:
    def __init__(self, name):
        self.name = name
        self.address = 0
        self.coordinates = 0
        self.info_for_dataframe = 0
        self.get_address()
        self.convert_address_to_coordinates(self.address)

    def get_address(self):
        if self.address == 0:
            self.address = input("Please enter your city, state, and zip code: ")
        else:
            pass

    def convert_address_to_coordinates(self, address):
        if self.coordinates == 0:
            self.coordinates = ArcGIS()
            self.coordinates = {"latitude": self.coordinates.geocode(address).latitude,
                                "longitude": self.coordinates.geocode(address).longitude}
        else:
            pass

    def verify_address_valid(self):
        pass

    def verify_address_in_usa(self):
        pass

    def verify_info_not_in_csv(self):
        pass

    def check_if_address_is_being_updated(self):
        pass

    def update_address(self):
        pass

    def get_info_for_dataframe(self):
        if self.info_for_dataframe == 0:
            self.info_for_dataframe = pandas.DataFrame([[self.name,
                                                         self.address,
                                                         self.coordinates["latitude"],
                                                         self.coordinates["longitude"]]],
                                                       columns=column_names)
        else:
            pass

    def add_to_dataframe(self):
        global df
        self.get_info_for_dataframe()
        df = df.append(self.info_for_dataframe)

    def update_in_dataframe(self):
        pass

