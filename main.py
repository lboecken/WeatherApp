from individual import Individual
from weather import Weather
from json_managment import IndividualDataManager


def main():
    pass


if __name__ == "__main__":
    main()

#test cases
John = Individual(name="John", address="Roswell, GA")
test = Weather(name=John)
Mary = Individual(name="Mary", address="Woodstock, GA")
test = Weather(name=Mary)
database = IndividualDataManager
database.add_user(John)
