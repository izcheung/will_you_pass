def welcome_message():
    print("Welcome to Swipe Right!")
    player_name = input("Please enter your character name: ")
    # player_gender = input("Please choose the letter that matches your character gender: /"
    #                       "ex: [F] Female, [M] Male, [O] Other")
    print(
        f"Welcome to Swipe Right {player_name}! You are a hopeless romantic who has been vying for the attention of the gorgeous class "
        "president. To get their attention, you have devised a plan to collect flowers and gift it to them on Valentine's day. Your first task is to go and collect 10 flowers.")
    input("Type anything to get started! ")
    return player_name


def make_character(player_name):
    player = {'name': player_name, 'level': 1, 'position': [3, 1], 'location': 'bedroom'}
    return player


def check_location_map(player):
    areas = {
            'bedroom': {
                    'rows': 8,
                    'columns': 7,
                    'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
                    'door': (6, 7)
            },
            'path': {
                    'rows': 10,
                    'columns': 7,
                    'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)],
                    'door': (4, 9)
            },
            'another_room': {
                    'rows': 4,
                    'columns': 12,
                    'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3)],
                    'door': (1, 2)
            }
    }
    for area, area_description in areas.items():
        if player['location'] == area:
            return area_description

