from geopy import ArcGIS


class Individual:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.coordinates = {}
        self.phone_number = phone_number
        self.json_package = {} ## likely to be droppped once SQL interaction is worked out.
        self.convert_address_to_coordinates(self.address)
        self.get_attributes_for_json_dump()

    def convert_address_to_coordinates(self, address):
        if self.coordinates == {}:
            self.coordinates = ArcGIS()
            self.coordinates = {"latitude": self.coordinates.geocode(address).latitude,
                                "longitude": self.coordinates.geocode(address).longitude}
        else:
            pass

    def get_attributes_for_json_dump(self): ##Likely to be dropped once SQL interaction is sorted out
        self.json_package = {
            "name": self.name,
            "address": self.address,
            "coordinates": self.coordinates,
            "phone number": self.phone_number
            }

