# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__obserations = []
        self.__latest_observation = ""


    def add_observation(self, observation: str):
        self.__obserations.append(observation)

    def latest_observation(self):
        return self.__obserations[-1] if len(self.__obserations) > 0 else ""

    def number_of_observations(self):
        return len(self.__obserations)

    def __str__(self):
        return f"{self.__name}, {len(self.__obserations)} observations"


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
