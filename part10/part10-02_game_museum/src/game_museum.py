# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games


class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        orig_list = super().list_games()
        filtered_list = [i for i in orig_list if i.year <= 1990]
        return filtered_list


if __name__ == "__main__":
    museum = GameMuseum()
    museum.add_game(ComputerGame("Final Fantasy VII","Square",1997))
    museum.add_game(ComputerGame("Doom","ID Software",1993)) 
    museum.add_game(ComputerGame("IK+","System 3",1987))
    museum.add_game(ComputerGame("Great Giana Sisters","Rainbow Arts",1987))
    museum.add_game(ComputerGame("Sim City 2000","Maxis",1993))
    museum.add_game(ComputerGame("Pool of Radiance","SSI",1988))
    for game in museum.list_games():
        print(game.name)