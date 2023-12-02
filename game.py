
import random


def welcome_message():
    """
    Customizes a welcome message for the player.

    :postcondition: uses the name of the player's character within the welcome message
    :return: the name of the player's character as a string
    """
    player_name = input("Please enter your character name: ")
    print(
        f"Welcome to Pass COMP1510 {player_name}! You are a hopeless student who achieved a final grade of 49.9% in COMP1510. Out of desperation, you made a devious plan to bribe Chris.  Your first task is to collect 5 Reese's chocolates.")
    input("Type anything to get started! ")
    return player_name


def make_character(player_name):
    """
    Creates a new character with the specified player name and default attributes.

    :param player_name: a string representing the name of the player's character
    :postcondition: creates a dictionary with the correct default attributes
    :return: a dictionary representing the player's character with the following attributes:
          - 'name': player's character name
          - 'level': initial level set at 1
          - 'intelligence': initial intelligence set to 0
          - 'HP': initial health set to 10
          - 'position': initial position represented as [row, column]
          - 'location': initial location set to 'tech_hub'
          - 'chocolate': initial number of chocolates set to 0

    >>> make_character('Irene')
    {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
    'chocolate': 0}
    """
    player = {'name': player_name, 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
              'chocolate': 0}
    return player


def give_location_description(player):
    """
    Returns a dictionary representing the description of a particular area.

    :param player: a dictionary representing a character created for this game
    :precondition: the player is provided in the correct format
    :postcondition: correctly return the dictionary that matches the character's current location
    :return: a dictionary with information on the character's current location
    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
    'location': 'tech_hub', 'chocolate': 0}
    >>> give_location_description(character)
    {
        'rows': 8,
        'columns': 7,
        'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                      (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
        'Chris': None
    }
    """
    areas = {
            'tech_hub': {
                    'rows': 8,
                    'columns': 7,
                    'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                                  (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
                    'Chris': None
            },
            'student_lounge': {
                    'rows': 10,
                    'columns': 7,
                    'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3), (6, 3),
                                  (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7),
                                  (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)],
                    'Chris': None
            },
            'room_645': {
                    'rows': 4,
                    'columns': 12,
                    'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3)],
                    'Chris': (6, 1)
            }
    }
    for area, area_description in areas.items():
        if player['location'] == area:
            return area_description


def add_map_boundaries(area_description):
    """
    Add outside boundaries to the specified map.

    :param area_description: a dictionary with information on the character's current location
    :precondition: area_description is provided in the correct format
    :postcondition: adds the boundary coordinates of the map to the map's list of obstacle coordinates
    >>> location_description = {
        'rows': 8,
        'columns': 7,
        'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                      (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
        'Chris': None
    }
    >>> add_map_boundaries(location_description)
    # ADD

    """
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


def generate_chocolate(player, area_description):
    """
    Returns a list of randomly generated coordinates of chocolates in the game.

    This function generates chocolates within the game area excluding the player's position and map obstacles.

    :param player: a dictionary representing a character created for this game
    :param area_description: a dictionary with information on the character's current location
    :precondition: player and area_description are provided in the correct format
    :precondition: character has greater than 0 HP
    :return: a list of tuple representing the coordinates of chocolates on the map
    """

    list_of_empty_coordinates = []
    for x_coordinate in range(area_description["columns"]):
        for y_coordinate in range(area_description["rows"]):
            if (x_coordinate, y_coordinate) not in area_description["obstacles"] and (x_coordinate, y_coordinate) != tuple(player['position']):
                list_of_empty_coordinates.append((x_coordinate, y_coordinate))
    chocolate_coordinates = random.sample(list_of_empty_coordinates, 5)
    return chocolate_coordinates


def print_map(player, area_description, chocolate_coordinates):
    """
    Prints a visual representation of the location's map.

    :param player: a dictionary representing a character created for this game
    :param area_description: a dictionary with information on the character's current location
    :param chocolate_coordinates: a list of tuples representing the coordinates of chocolates in the game
    :precondition: player, area_description, and chocolate_coordinates are in the correct format
    :precondition: character has greater than 0 HP
    # ADD
    """
    for row in range(area_description["rows"]):
        for column in range(area_description["columns"]):
            coordinate = [column, row]

            if coordinate == player['position']:
                print('*', end="")
            elif tuple(coordinate) in area_description["obstacles"]:
                print('#', end="")
            elif tuple(coordinate) in chocolate_coordinates:
                print('!', end="")
            elif tuple(coordinate) == area_description["Chris"]:
                print('C', end="")
            else:
                print(' ', end="")
        print()
    print(f'You are at position {player["position"]}\n')


def get_user_choice(player):
    """
    Returns the direction that the user choose.

    :precondition: user input must be a number associated with the direction (ie: not "1" and not "North")
    :precondition: character has greater than 0 HP
    :postcondition: returns the direction after acquiring a correct input from the user
    :return: a string representing the direction chosen by the user
    """
    while True:
        direction = input('[1] North, [2] South, [3] East, [4] West, [S] Stats\nPlease enter the number that corresponds to/'
                        'the direction you want to go: ')
        if direction in ['1', '2', '3', '4']:
            return direction
        # elif direction in ['S', 's']:
        #     print_stats(player)
        else:
            print("Invalid direction. ")


def validate_move(player, area_description, direction):
    """
    Checks if a move in the specified direction is valid for the player.

    :param player: a dictionary representing a character created for this game
    :param area_description: a dictionary with information on the character's current location
    :param direction: a string representing the direction chosen by the user
    :precondition: the player, area_description, and direction are provided in the correct format
    :precondition: character has greater than 0 HP
    :postcondition: correctly check whether the move will result in a valid coordinate (within bounds and no obstacle)
    :return: a boolean - True if the move in the specified direction is valid and False otherwise
    #ADD
    """

    new_coordinate = player["position"].copy()
    if direction == "1":
        new_coordinate[1] -= 1
    elif direction == "2":
        new_coordinate[1] += 1
    elif direction == "3":
        new_coordinate[0] += 1
    elif direction == "4":
        new_coordinate[0] -= 1

    if tuple(new_coordinate) in area_description["obstacles"]:
        return False
    else:
        return True


def move_character(player, direction):
    """
    Updates the character's position in the character dictionary.

    :param player: a dictionary representing the character created for this game
    :param direction: a string representing the direction chosen by the user
    :precondition: move has been validated to be within the board bounds
    :precondition: character and direction are provided in the correct format
    :precondition: character has greater than 0 HP
    :postcondition: correctly change the character coordinates based on the direction input
    #ADD
    """
    if direction == '1':
        player['position'][1] -= 1
    if direction == '2':
        player['position'][1] += 1
    if direction == '3':
        player['position'][0] += 1
    if direction == '4':
        player['position'][0] -= 1

    return player


def quiz_probability():
    """
    Generate a surprise pop quiz 20% of the time after each move.

    :precondition: user must have had moved to a new coordinate
    :precondition: character has greater than 0 HP
    :postcondition: randomly generate surprise pop quizzes 20% of the time for each move
    :return: True when the probability of getting a quiz is equal to 1 (out of 5 numbers), and False otherwise.
    """
    probability_of_getting_a_quiz = random.randint(1, 5)
    if probability_of_getting_a_quiz == 1:
        return True
    else:
        return False


def make_quiz_questions():
    """
    Creates a dictionary of surprise quiz questions.

    :precondition: character has greater than 0 HP
    :postcondition: correctly creates a dictionary of questions as keys, and the correct answer as the value
    :return: a dictionary of surprise pop quiz questions.
    """

    surprise_questions = {"'When are you getting married?'": 1, "*pinching your cheeks*": 2,
                         "'Have you recently gained weight?'": 3,
                         "'My son is sooo successful blah blah..., what are you doing these days?'": 4}
    return surprise_questions


def surprise_pop_quiz(player, surprise_questions):
    print("You ran into your aunt!")
    random_attack = random.choice(list(surprise_questions.keys()))
    print(f"Your aunt attacks with: {random_attack}")
    dodge = input("Guess the right number (1 to 4) to run away: ")
    correct_number = random.randint(1, 4)
    if dodge == correct_number:
        player['intelligence'] += 25
        print(f"You brush it off and your intelligence is now {player['intelligence']}!")
    else:
        player['HP'] -= surprise_questions.get(random_attack)
        if player['HP'] > 0:
            print(f'Your HP takes a hit! -{surprise_questions.get(random_attack)} points. Current HP is {player['HP']}\n')

# player, area_description
# chocolate_coordinates = [(2, 0), (6, 6), (0, 1), (3, 2), (3, 0)]





def level_up_to_3(player, surprise_questions):
    print("YOU LEVELED UP TO LEVEL 3!\nIt's time...be careful, there are some HARD pop quizzes waiting to ambush you here... find Chris")
    player["level"] += 1
    player["HP"] += 20
    player["location"] = "room_645"
    player["position"] = [1, 2]
    chocolate_coordinates = []
    for each_attack_move in surprise_questions:
        surprise_questions[each_attack_move] *= 2
    return chocolate_coordinates


def print_stats(player):
    print(player)


def level_up_to_2(player, surprise_questions):
    print("YOU LEVELED UP TO LEVEL 2!")
    player["level"] += 1
    player["HP"] += 10
    player["location"] = "student_lounge"
    player["position"] = [3, 1]
    for each_attack_move in surprise_questions:
        surprise_questions[each_attack_move] *= 2
    area_description = give_location_description(player)
    add_map_boundaries(area_description)
    chocolate_coordinates = generate_chocolate(player, area_description)
    return chocolate_coordinates


# player, chocolate_coordinates
def pick_up_chocolate(player, chocolate_coordinates):
    if tuple(player["position"]) in chocolate_coordinates:
        player["chocolate"] += 1
        print(f"\nYou picked up a Reese's chocholate! You now have {player["chocolate"]}.\n")
        chocolate_coordinates.remove(tuple(player["position"]))
        return chocolate_coordinates


def unlock_map():
    pass


def is_alive(player):
    if player["HP"] > 0:
        return True
    else:
        print(f'Your HP has hit rock bottom. GAME OVER!')
        return False

def check_officially_dating():
    pass


def check_level(player, surprise_questions):
    if player['chocolate'] == 5 and player['level'] == 1:
        chocolate_coordinates = level_up_to_2(player, surprise_questions)
        return chocolate_coordinates

    elif player['chocolate'] == 10 and player['level'] == 2:
        chocolate_coordinates = level_up_to_3(player, surprise_questions)
        return chocolate_coordinates



def number_of_final_exam_attempts(player):
    if player['intelligence'] >= 1000:
        player['HP'] = 3
    elif player['intelligence'] >= 500:
        player['HP'] = 2
    else:
        player['HP'] = 1


def final_exam(player):
    number_of_final_exam_attempts(player)
    print(f"\n\nWelcome to COMP1510 mWAHAHAH, it is I, Chris! Can you pass this final test? Based on your points, you have {player['HP']} tries.")
    correct_answers = 0
    questions = {
        "You made slight eye contact! What is my favourite chocolate?\n[1]KitKat\n[2]Snickers\n[3]Reese's chocolate\n[4]Toblerone\n": '3',
        "Does pineapple belong on my pizza?\n[1]It's not my first pick\n[2]Pineapple on pizza is *chef's kiss*\n[3]Food sounds good to me\n[4]That's an abomination!\n": '4',
        "Are you going to pass my course?\n[1]Yes\n[2]No\n": "1"}

    for question, answer in questions.items():
        if is_alive(player) and correct_answers < 3:
            question_number = input(question)
            if question_number == answer:
                print("I see that you pay attention in class. Very good! Everyone give a round of applause!\n")
                correct_answers += 1
            else:
                player['HP'] -= 1
                print("Oof, not quite. But nice try.")
    if correct_answers == 3:
        officially_dating = True
        return officially_dating
    else:
        print("You FAIL")


# "Who is feeling brave today?"
# "You made slight eye contact!"


def game():
    player_name = welcome_message()
    character = make_character(player_name)
    current_location = give_location_description(character)
    add_map_boundaries(current_location)
    chocolate_coordinates = generate_chocolate(character, current_location)
    attack_moves = make_quiz_questions()
    print_map(character, current_location, chocolate_coordinates)
    officially_dating = False
    while is_alive(character) and not officially_dating:
        direction = get_user_choice(character)
        valid_move = validate_move(character, current_location, direction)
        if valid_move:
            move_character(character, direction)
            pick_up_chocolate(character, chocolate_coordinates)
            # if quiz_probability():
                # surprise_pop_quiz(character, attack_moves)
            # chocolate_coordinates = check_level(character, attack_moves, current_location)
            if character['chocolate'] == 5 and character['level'] == 1:
                chocolate_coordinates = check_level(character, attack_moves)

            elif character['chocolate'] == 10 and character['level'] == 2:
                chocolate_coordinates = check_level(character, attack_moves)
            current_location = give_location_description(character)
            add_map_boundaries(current_location)
            print_map(character, current_location, chocolate_coordinates)
            if character["position"] == [6, 1] and character["location"] == "room_645":
                officially_dating = final_exam(character)

            # if is_alive(character):
            #     officially_dating = check_officially_dating()
            #     if officially_dating:
            #         print("CONGRATULATIONS. YOU GOT ARE COUPLED!")
        else:
            print("\nYou can't go there!")



def main():
    game()


main()
