# import pandas as pd
#import individual
import json

# TODO Backend json interaction Class

class IndividualDataManager:
    def __init__(self):
        pass

    @staticmethod
    def add_user():
        with open("individuals.json", "a") as json_file:
            p
            print(json_file)




    def verify_address_valid(self):
        pass#check if individual.coordinates["Latitude] or ["Longitude"] exists. (This might need to be in individual)

    def verify_info_not_in_json(self):
        pass #check if data already in JSON; pass if it is; throw message to user that data already exists and will be overwritten.

    def check_if_address_is_being_updated(self):
        pass #this needs to go to twilio -> Ask "would you like to update your address?"

    def update_some_information(self):
        pass #create ways to update only part of a user.
