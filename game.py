
import random

def welcome_message():
    print("Welcome to Swipe Right!")
    player_name = input("Please enter your character name: ")
    print(
        f"Welcome to Swipe Right {player_name}! You are a hopeless romantic who has been vying for the attention of the gorgeous class "
        "president. To get their attention, you have devised a plan to collect flowers and gift it to them on Valentine's day. Your first task is to go and collect 10 flowers.")
    input("Type anything to get started! ")
    return player_name


def make_character(player_name):
    player = {'name': player_name, 'level': 1, 'maturity': 0, 'self-esteem': 10, 'position': [3, 1], 'location': 'bedroom', 'flowers': 0}
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



def print_location_map(player, area_description, flower_coordinates):

    for row in range(area_description["rows"]):
        for column in range(area_description["columns"]):
            coordinate = [column, row]
            if coordinate == player['position']:
                print('*', end="")
            elif tuple(coordinate) in area_description["obstacles"]:
                print('#', end="")
            elif tuple(coordinate) in area_description["door"]:
                print('X', end="")
            elif tuple(coordinate) in flower_coordinates:
                print('!', end="")
            else:
                print(' ', end="")
        print()
    print(f'You are at position {player["position"]}')
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
            print("Invalid direction. ")


def validate_move(player, area_description, direction):
    new_coordinate = player["position"].copy()
    if direction == "1":
        new_coordinate[1] -= 1
    elif direction == "2":
        new_coordinate[1] += 1
    elif direction == "3":
        new_coordinate[0] += 1
    elif direction == "4":
        new_coordinate[0] -= 1
    # else?

    if tuple(new_coordinate) in area_description["obstacles"]:
        return False
    else:
        return True


def move_character(player, direction):
    if direction == '1':
        player['position'][1] -= 1
    if direction == '2':
        player['position'][1] += 1
    if direction == '3':
        player['position'][0] += 1
    if direction == '4':
        player['position'][0] -= 1

    return player


def run_into_relatives():
    chance_of_running_into_relatives = random.randint(1, 5)
    if chance_of_running_into_relatives == 1:
        return True
    else:
        return False


def auntie_encounter(player):
    aunt_attack_moves = {"'When are you getting married?'": 1, "*pinching your cheeks*": 2, "'Have you recently gained weight?'": 3, "'My son is sooo successful blah blah..., what are you doing these days?'": 4}
    print("You ran into your aunt!")
    random_attack = random.choice(list(aunt_attack_moves.keys()))
    print(f"Your aunt attacks with: {random_attack}")
    dodge = input("Guess the right number (1 to 4) to run away: ")
    correct_number = random.randint(1, 4)
    if dodge == correct_number:
        player['maturity'] += 25
        print(f"You brush it off and your maturity is now {player['maturity']}!")
    else:
        player['self-esteem'] -= aunt_attack_moves.get(random_attack)
        print(f'Your self-esteem takes a hit! -{aunt_attack_moves.get(random_attack)} points. Current HP is {player['self-esteem']}')


def level_up(player, aunt_attack_moves):
    if player["maturity"] >= 500:
        print("You leveled up to Level 3!")
        player["level"] += 1
        player["self-esteem"] += 30
        for each_attack_move in aunt_attack_moves:
            aunt_attack_moves[each_attack_move] *= 4
        unlock_map()

    elif player["maturity"] >= 250:
        print("You leveled up to Level 2!")
        player["level"] += 1
        player["self-esteem"] += 20
        for each_attack_move in aunt_attack_moves:
            aunt_attack_moves[each_attack_move] *= 3
        unlock_map()


    elif player["maturity"] >= 100:
        print("You leveled up to Level 1!")
        player["level"] += 1
        player["self-esteem"] += 10
        for each_attack_move in aunt_attack_moves:
            aunt_attack_moves[each_attack_move] *= 2
        unlock_map()


def unlock_map():
    pass


# Issues

def change_location(player):
    if player['position'] == [5, 6] and player['location'] == 'bedroom':
        player['location'] = 'path'
        player['position'] = [3, 1]
    if player['position'] == [3, 1] and player['location'] == 'path':
        player['location'] = 'bedroom'
        player['position'] = [5, 6]
    if player['position'] == [4, 9] and player['location'] == 'path':
        player['location'] = 'another_room'
        player['position'] = [1, 2]
    if player['position'] == [1, 2] and player['location'] == 'another_room':
        player['location'] = 'path'

    return player



def game():
    player_name = welcome_message()
    character = make_character(player_name)
    officially_dating = False
    while not officially_dating:
        current_location = check_location_map(character)
        add_map_boundaries(current_location)
        flower_coordinates = generate_flowers(character, current_location)
        print_location_map(character, current_location, flower_coordinates)
        direction = get_user_choice()
        valid_move = validate_move(character, current_location, direction)
        if valid_move:
            move_character(character, direction)
            character = change_location(character)
            print_location_map(character, current_location, flower_coordinates)
            if run_into_relatives():
                auntie_encounter(character)
        else:
            print("\nYou can't go there!")
    print("Congratulations!")

def main():
    game()


main()
