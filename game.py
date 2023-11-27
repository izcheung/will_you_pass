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


def add_map_boundaries(area_description):
    y_axis = area_description["rows"]
    x_axis = area_description["columns"]

    first_last_rows = [0, y_axis - 1]
    for row in first_last_rows:
        for column in range(x_axis):
            wall = (column, row)
            area_description["obstacles"].append(tuple(wall))

    first_last_columns = [0, x_axis - 1]
    for column in first_last_columns:
        for row in range(y_axis):
            wall = (column, row)
            if wall in area_description["obstacles"]:
                continue
            else:
                area_description["obstacles"].append(tuple(wall))


def print_location_map(player, area_description):
    print(player["position"])
    for row in range(area_description["rows"]):
        for column in range(area_description["columns"]):
            coordinate = [column, row]
            if coordinate == player['position']:
                print('*', end="")
            elif tuple(coordinate) in area_description["obstacles"]:
                print('#', end="")
            elif tuple(coordinate) in area_description["door"]:
                print('X', end="")
            else:
                print(' ', end="")
        print()
    print()


#     # north_wall = coordinate[0] == 0
#     # west_wall = coordinate[1] == 0
#     # east_wall = coordinate[0] == columns - 1
#     # south_wall = coordinate[1] == rows - 1
#     # if north_wall or south_wall:
#     #     print('-', end='')
#     # elif east_wall or west_wall:
#     #     print('|', end='')

# Criteria 7


def get_user_choice():
    while True:
        direction = input('[1] North, [2] South, [3] East, [4] West\nPlease enter the number that corresponds to/'
                        'the direction you want to go: ')
        if direction in ['1', '2', '3', '4']:
            return direction
        else:
            print("Invalid direction.")


