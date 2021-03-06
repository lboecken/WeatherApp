import pandas as pd
import individual

# TODO Add CSV File to store user data
# TODO Backend CSV interaction Class

column_names = ["Name", "City, State, Zip", "Latitude", "Longitude"]


class IndividualDataframe(pd.DataFrame):
    def __init__(self, master=None):
        super.__init__(master)
        print("Hello World")

    def verify_address_valid(self):
        pass

    def verify_info_not_in_csv(self):
        pass

    def check_if_address_is_being_updated(self):
        pass

    def update_address(self):
        pass

    def add_to_dataframe(self):
        individual.Individual.get_info_for_dataframe()  # TODO can this be done using a decorator?
        #df.append(individual.Individual.info_for_dataframe)  # TODO

    def update_in_dataframe(self):
        pass
