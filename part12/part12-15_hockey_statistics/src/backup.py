# Write your solution here
import json


def reader(filename):
    with open(filename) as f:
        data = f.read()

    return json.loads(data)

class DataProcessor:
    def __init__(self, filename):
        self.__filename = filename
        self.__players = reader(self.__filename)

    def __str__(self):
        return ((i["name"], i["team"], i["goals"]) for i in self.__players)

    def get_players(self):
        return self.__players



class HockeyStatisticsApplication:
    def __init__(self):
        filename = input("file name: ")
        self.__stats = DataProcessor(filename).get_players()


    def help(self):
        print("")
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")


    def search_for_player(self):
        name = input("name: ")
        print("")
        for i in self.__stats:
            if i["name"] == name:
                print(f"{i["name"]:21}{i["team"]:6}{i["goals"]} + {i["assists"]} =  {i["goals"] + i["assists"]}")

    def get_teams(self):
        print("\n".join(sorted(set([i["team"] for i in self.__stats]))))

    def get_countries(self):
        print("\n".join(sorted(set([i["nationality"] for i in self.__stats]))))

    def get_players_in_team(self):
        team = input("team: ")
        print("")
        for i in self.__stats:
            if i["team"] == team:
                print(f"{i["name"]:21}{i["team"]:6}{i["goals"]} + {i["assists"]} =  {i["goals"] + i["assists"]}")

    def get_players_from_country(self):
        country = input("nationality: ")
        print("")
        for i in self.__stats:
            if i["nationality"] == country:
                print(f"{i["name"]:21}{i["team"]:6}{i["goals"]} + {i["assists"]} =  {i["goals"] + i["assists"]}")


    def get_most_points(self):
        n = int(input("how many: "))
        x = sorted([i for i in self.__stats], key=lambda p: p["goals"]+p["assists"], reverse=True)
        for i in x[n]:
            print(f"{i["name"]:21}{i["team"]:6}{i["goals"]} + {i["assists"]} =  {i["goals"] + i["assists"]}")

    def execute(self):
        print(f"read the data of {len(self.__stats)} players")

        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.search_for_player()
            if command == "2":
                self.get_teams()
            if command == "3":
                self.get_countries()
            if command == "4":
                self.get_players_in_team()
            if command == "5":
                self.get_players_from_country()
            if command == "6":
                self.get_most_points()
            if command == "7":
                self.get_most_goals()
            
            # else:
            #     print("Invalid request, stopping application...")
            #     break



application = HockeyStatisticsApplication()
application.execute()