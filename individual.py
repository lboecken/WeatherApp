from geopy import ArcGIS

class ConstructIndividualFromDict:
    def __init__(self, dict):
        pass

class ConstructIndividualFromGEO:
    def __init__(self):


class Individual:
    def __init__(self, name, address, phone_number=0):
        self.name = name
        self.address = address
        self.coordinates = {}
        self.phone_number = phone_number
        self.json_package = {}
        self.convert_address_to_coordinates(self.address)
        self.get_attributes_for_json_dump()

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


