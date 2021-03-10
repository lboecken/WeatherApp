from individual import Individual
from weather import Weather
from json_managment import IndividualDataManager
import pprint
import json


def main():
    pass


if __name__ == "__main__":
    main()

#test cases
John = Individual(name="John")
test = Weather(name=John)
Mary = Individual(name="Mary")
test = Weather(name=Mary)
database = IndividualDataManager
database.add_user()