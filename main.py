from individual import Individual
from weather import Weather
import pprint


def main():
    pass


if __name__ == "__main__":
    main()


John = Individual(name="John")
test = Weather(name=John)
pprint.pprint(test.daily)