import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        
        if player_dict["nationality"] == "FIN":

            player = Player(
                player_dict
            )
            
            players.append(player)

    print("Players from FIN:\n")

    for player in players:
        print(player)
        

if __name__ == "__main__":
    main()
