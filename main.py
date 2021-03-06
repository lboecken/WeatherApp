from individual import Individual
from data_managment import IndividualDataframe
from weather import Weather
import pandas as pd


def main():
    pass


if __name__ == "__main__":
    main()


John = Individual(name="John")
test = Weather(name=John)
test.openweather_api_pull()
print(test.sky)
