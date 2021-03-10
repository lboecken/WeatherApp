from geopy import ArcGIS


class Individual:
    def __init__(self, name, phone_number=0):
        self.name = name
        self.address = ""
        self.coordinates = {}
        self.phone_number = phone_number
        self.json_package = {}
        self.get_address()
        self.convert_address_to_coordinates(self.address)
        self.prepare_attributes_for_json_dump()

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

    def get_attributes_for_json_dump(self):
        self.json_package = {
            self.name: {
                "address": self.address,
                "coordinates": self.coordinates,
                "phone number": self.phone_number
            }
        }


