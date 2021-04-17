import json
import collections


# TODO Backend json interaction Class


class IndividualDataManager:
    def __init__(self):
        pass

    def add_user(self, user):
        if self.verify_user_exists_in_json(user):
            pass
        else:
            with open("individuals.json", "r") as json_file:
                data = json.load(json_file)
                data["USERS"][user["name"]] = user

            with open("individuals.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

    def verify_user_exists_in_json(self, user):
        with open("individuals.json", "r") as json_file:
            data = dict(json.load(json_file))
            return data["USERS"].__contains__(user["name"])

    def delete_user(self, user):
        with open("individuals.json", "r") as json_file:
            data = dict(json.load(json_file))
            data["USERS"].__delitem__(user["name"])

        with open("individuals.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def update_user_information(self):
        def update_address():
            pass

        def update_phone_number():
            pass

        def update_name():
            pass

        pass  # create ways to update only part of a user.
