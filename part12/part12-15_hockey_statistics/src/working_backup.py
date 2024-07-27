import json

def load_data(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def printer(player):
    print(f'{player["name"]:<20} {player["team"]:<4} {player["goals"]:>2} + {player["assists"]:>2} = {player["goals"] + player["assists"]:>3}')


class HockeyStatisticsApplication:
    def __init__(self):
        file_name = input("file name: ")
        self.__stats = load_data(file_name)


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
        for player in self.__stats:
            if player["name"].lower() == name.lower():
                printer(player)
                return
        print("Player not found")

    def get_teams(self):
        teams = sorted({player["team"] for player in self.__stats})
        for team in teams:
            print(team)

    def get_countries(self):
        countries = sorted({player["nationality"] for player in self.__stats})
        for country in countries:
            print(country) 

    def get_players_in_team(self):
        team = input("team: ")
        result = sorted(self.__stats, key=lambda x: x["goals"] + x["assists"], reverse=True)
        print("")
        for player in result:
            if player["team"] == team:
                printer(player)

    def get_players_from_country(self):
        country = input("country: ")
        result = sorted(self.__stats, key=lambda x: x["goals"] + x["assists"], reverse=True)
        print("")
        for player in result:
            if player["nationality"] == country:
                printer(player)

    def get_most_points(self):
        num = int(input("how many: "))
        player = sorted(self.__stats, key=lambda x: (x["goals"] + x["assists"], x["goals"]), reverse=True)[:num]
        for p in player:
            printer(p)

    def get_most_goals(self):
        num = int(input("how many: "))
        player = sorted(self.__stats, key=lambda x: (x["goals"], -x["games"]), reverse=True)[:num]
        for p in player:
            printer(p)


    def execute(self):
        print(f"read the data of {len(self.__stats)} players")

        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.get_players_in_team()
            elif command == "5":
                self.get_players_from_country()
            elif command == "6":
                self.get_most_points()
            elif command == "7":
                self.get_most_goals()
            else:
                print("Invalid command")


application = HockeyStatisticsApplication()
application.execute()
