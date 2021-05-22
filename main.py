from individual import Individual
from weather import Weather
from json_managment import IndividualDataManager
from sqldb import DatabaseManager

def main():
    test = DatabaseManager()
    location = (5, 'Home', '608 Lauder Circle, Woodstock, GA', 34.085950, -84.457790)
    test.add_new_location_for_user(location)

if __name__ == "__main__":
    main()

#test cases



