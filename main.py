from individual import Individual
from weather import Weather
from json_managment import IndividualDataManager


def main():
    pass


if __name__ == "__main__":
    main()

#test cases
John = Individual(name="John Doe", address="Roswell, GA", phone_number=5555555555)
test = Weather(name=John)
Mary = Individual(name="Mary Jane", address="Woodstock, GA", phone_number=5555555555)
test = Weather(name=Mary)
database = IndividualDataManager()
database.add_user(Mary.json_package)
database.add_user(John.json_package)


