"""
Irene Cheung
A01349998
"""

import random
import itertools


def welcome_message():
    """
    Customizes a welcome message for the player using their name.

    :postcondition: uses the name of the player's character within the welcome message
    :return: the name of the player's character as a string
    """
    player_name = ""
    while len(player_name) == 0:
        player_name = input("Please enter your character name: ")
    print(f"Welcome to 'Pass COMP1510' {player_name}! You are a hopeless student with an average of 49.9% in COMP1510. "
          f"Out of desperation, you make a devious plan to bribe Chris with his favourite chocolates to pass his "
          f"course. Your task is to collect 10 Reese's chocolates and then deliver it to him.")
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

    >>> make_character('John')
    {'name': 'John', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
'chocolate': 0}
    """
    player = {'name': player_name, 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
              'chocolate': 0}
    return player


def add_map_boundaries(area_description):
    """
    Add outside boundaries to the specified map.

    :param area_description: a dictionary with information on the character's current location
    :precondition: area_description is provided in the correct format
    :postcondition: adds the boundary coordinates of the map to the map's list of obstacle coordinates
    >>> description_of_area = {'rows': 8, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3),\
(6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)], 'Chris': None}
    >>> add_map_boundaries(description_of_area)
    >>> updated_obstacles = description_of_area["obstacles"]
    >>> updated_obstacles == [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), \
(1, 7), (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 7), (1, 7), (2, 7), (3, 7),\
 (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 1), (6, 5), (6, 6)]
    True

    >>> description_of_area = {'rows': 10, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), \
(5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7), (1, 8),\
 (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)], 'Chris': None}
    >>> add_map_boundaries(description_of_area)
    >>> updated_obstacles = description_of_area["obstacles"]
    >>> updated_obstacles == [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), \
(6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9),\
 (5, 9), (6, 9), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), \
 (5, 9), (6, 9), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (6, 5), (6, 6)]
    True
    """
    y_axis = int(area_description["rows"])
    x_axis = int(area_description["columns"])

    wall_coordinates = []

    area_description["obstacles"] += wall_coordinates
    for row in [0, y_axis - 1]:
        for column in range(x_axis):
            wall = (column, row)
            area_description["obstacles"].append(tuple(wall))

    for column in [0, x_axis - 1]:
        for row in range(y_axis):
            wall = (column, row)
            if wall in area_description["obstacles"]:
                continue
            else:
                area_description["obstacles"].append(tuple(wall))


def generate_chocolate(player, area_description):
    """
    Returns a list of randomly generated coordinates of chocolates in the game.

    This function generates chocolates coordinates within the game area excluding the player's position and map
    obstacles.

    :param player: a dictionary representing a character created for this game
    :param area_description: a dictionary with information on the character's current location
    :precondition: area_description must be one of tech_hub, student_lounge, or room_645
    :precondition: player and area_description are provided in the correct format
    :precondition: character has greater than 0 HP
    :postcondition: randomly generates a chocolate coordinate within the board, not in an obstacle or player coordinate,
     and not repeated
    :return: a list of five tuples representing the coordinates of chocolates on the map
    """
    list_of_empty_coordinates = []

    for x_coordinate in range(area_description["columns"]):
        for y_coordinate in range(area_description["rows"]):
            if (x_coordinate, y_coordinate) not in area_description["obstacles"] and (
                    x_coordinate, y_coordinate) != tuple(player['position']):
                list_of_empty_coordinates.append((x_coordinate, y_coordinate))
    chocolate_coordinates = random.sample(list_of_empty_coordinates, 5)
    area_description["chocolate_coordinates"] = chocolate_coordinates


def initialize_map(player):
    """
    Initialize the three map locations by adding map boundaries and chocolate coordinates.

    :param player: a string representing the name of the player's character
    :precondition: player must be in the correct format
    :precondition: generate_chocolate and add_map_boundaries functions work as intended
    :postcondition: updated the area dictionary to include map boundaries and randomly generated chocolate coordinates
    :return: a dictionary with nested dictionaries representing the map details for each level
    """
    areas = {'tech_hub': {'rows': 8, 'columns': 7,
                          'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                                        (1, 6), (1, 7),
                                        (2, 7), (3, 7), (4, 7)], 'Chris': None},
             'student_lounge': {'rows': 10, 'columns': 7,
                                'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                              (6, 3), (5, 4), (6, 4),
                                              (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7), (1, 8),
                                              (2, 8), (5, 8), (6, 8),
                                              (1, 9), (2, 9), (5, 9), (6, 9)], 'Chris': None},
             'room_645': {'rows': 4, 'columns': 12,
                          'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3)],
                          'Chris': (6, 1)}}
    for area, area_description in areas.items():
        add_map_boundaries(area_description)
        if area != "room_645":
            generate_chocolate(player, area_description)
        else:
            area_description["chocolate_coordinates"] = []
    return areas


def give_location_description(player, areas):
    """
    Returns a dictionary representing the description of a particular area.

    :param player: a dictionary representing a character created for this game
    :param areas: a dictionary containing nested dictionaries with information for the three game maps
    :precondition: the player and areas is provided in the correct format
    :precondition: player location must be one of 'tech_hub', 'student_lounge', or 'room_645'
    :postcondition: correctly return the dictionary that matches the character's current location
    :return: a dictionary with information on the character's current location
    """
    for area, area_description in areas.items():
        if player['location'] == area:
            return area_description


def print_map(player, area_description):
    """
    Prints a visual representation of the location's map.

    :param player: a dictionary representing a character created for this game
    :param area_description: a dictionary with information on the character's current location
    :precondition: player, area_description, and chocolate_coordinates are in the correct format
    :precondition: character has greater than 0 HP
    :postcondition: print the map with the correct representations for obstacle, chris, chocolates, and position
    """
    for row in range(area_description["rows"]):
        for column in range(area_description["columns"]):
            coordinate = [column, row]

            if coordinate == player['position']:
                print('*', end="")
            elif tuple(coordinate) in area_description["obstacles"]:
                print('#', end="")
            elif tuple(coordinate) in area_description["chocolate_coordinates"]:
                print('!', end="")
            elif tuple(coordinate) == area_description["Chris"]:
                print('C', end="")
            else:
                print(' ', end="")
        print()
    print(f'You are at position {player["position"]}\n')


def get_user_choice():
    """
    Returns the direction that the user choose.

    :precondition: user input must be a number associated with the direction (ie: must be "1", "2", "3", or "4")
    :precondition: character HP must be greater than 0
    :postcondition: returns the direction after acquiring a correct input from the user
    :return: a string representing the direction chosen by the user
    """
    while True:
        direction = input('[1] North, [2] South, [3] East, [4] West\nPlease enter the number that corresponds to/'
                          'the direction you want to go: ')
        if direction in ['1', '2', '3', '4']:
            return direction
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

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': \
    'student_lounge', 'chocolate': 0}
    >>> location_description = { 'rows': 10, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), \
    (2, 2), (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7),\
     (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)], 'Chris': None, 'chocolate_coordinates':\
      [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)] }
    >>> user_choice_direction = 1
    >>> validate_move(character, location_description, user_choice_direction)
    True

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 2], 'location': \
    'student_lounge', 'chocolate': 0}
    >>> location_description = { 'rows': 10, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), \
    (2, 2), (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7),\
     (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)], 'Chris': None, 'chocolate_coordinates': \
     [(1, 3), (2, 3), (4, 4), (4, 5), (2, 4)]}
    >>> user_choice_direction = 2
    >>> validate_move(character, location_description, user_choice_direction)
    False
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
    :return: the player dictionary with an updated position

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 2], \
'location': 'student_lounge', 'chocolate': 0}
    >>> user_choice_direction = '1'
    >>> move_character(character, user_choice_direction)
    {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 1], 'location': 'student_lounge', \
'chocolate': 0}

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 2], 'location': \
'student_lounge', 'chocolate': 0}
    >>> user_choice_direction = '3'
    >>> move_character(character, user_choice_direction)
    {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [2, 2], 'location': 'student_lounge',\
 'chocolate': 0}
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
    Creates a dictionary of surprise quiz questions as the key and the damage points as the value.

    :precondition: character has greater than 0 HP
    :postcondition: correctly creates a dictionary of questions as keys, and the correct answer as the value
    :return: a dictionary of surprise pop quiz questions

    >>> question_choices = make_quiz_questions()
    >>> print(question_choices)
    {'Is the dress blue/black or \
white/gold?\\nChoices:\\n1: Blue/black\\n2: White/gold:\\n3: Neither\\n4: Both': 2, 'Are hot dogs \
sandwiches?\\nChoices:\\n1: Yes\\n2: No, they are tacos.\\n3: No, they cannot be classified as anything other \
than hot dogs.\\n4: Maybe, it depends on my mood': 4, 'Why are pizza boxes square but pizzas are \
circular?\\nChoices:\\n1: Because it is cheaper\\n2: Because it is easier to take out a slice when the box is \
square.\\n3: Because nothing makes sense in the world.\\n4: Because why not?': 3, 'Is the opposite of opposite \
the same or opposite?\\nChoices:\\n1: Same\\n2: Opposite\\n3: Opposite opposite\\n4: Opposite squared': 2}

    """
    surprise_questions = {
        'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
        'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
        'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
        'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it is '
        'easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4: Because '
        'why not?': 3,
        'Is the opposite of opposite the same or opposite?\nChoices:\n1: Same\n2: Opposite\n3: Opposite opposite\n4: '
        'Opposite squared': 2}
    return surprise_questions


def surprise_pop_quiz(player, surprise_questions):
    """
    Generates a surprise pop quiz where the user must guess a number between 1 and 4 inclusive.

    If user makes an incorrect guess, HP will be deducted by 1. If the guess is correct, there will be no deduction \
    and player will gain 25 intelligence points.

    :param player: a dictionary representing the character created for this game
    :param surprise_questions: a dictionary of surprise pop quiz questions
    :precondition: player and surprise_questions are provided in the correct format
    :precondition: character has greater than 0 HP
    :postcondition: correctly check whether the user guessed the right integer between 1 and 4 inclusive
    :postcondition: one HP point is deducted for a wrong answer and 25 intelligence points are earned for a right answer
    """
    random_attack = random.choice(list(surprise_questions.keys()))
    print(f"You made slight eye contact! {random_attack}")
    correct_number = random.randint(1, 4)
    user_answer = ''
    while user_answer not in ['1', '2', '3', '4']:
        user_answer = input(
            "Guess a number between 1 and 4 inclusive that corresponds to your answer. (PS: answer is random): ")
    if user_answer == correct_number:
        player['intelligence'] += 25
        print(f"That is correct! Your intelligence is now {player['intelligence']} points!")
    else:
        player['HP'] -= surprise_questions.get(random_attack)
        if player['HP'] > 0:
            print(
                f"Your HP takes a hit! -{surprise_questions.get(random_attack)} points. Current HP is"
                f" {player['HP']}.\n")


def level_up_to_3(player, surprise_questions):
    """
    Sets up the game for when character advances to level 3.

    :param player: a dictionary representing the character created for this game
    :param surprise_questions: a dictionary of surprise pop quiz questions
    :precondition: player and surprise_questions are provided in the correct format
    :preconditiion: player must be at level 2 and have 10 chocolates
    :precondition: character has greater than 0 HP
    :postcondition: increase player level by 1, HP by 20
    :postcondition: set location to room 645 with no chocolate coordinates and position to [1, 2]
    :postcondition: double the damage power for each surprise question
    :return: an empty list of chocolate coordinates

    >>> character = {'name': 'Irene', 'level': 2, 'intelligence': 100, 'HP': 10, 'position': [3, 1], 'location': \
'student_lounge', 'chocolate': 10}
    >>> questions = {"Is the dress blue/black or white/gold?": 4, "Are hot dogs sandwiches?": 8, \
"Why are pizza boxes square but pizzas are circular?": 6, "Is the opposite of opposite the same or opposite": 4}
    >>> level_up_to_3(character, questions)
    YOU LEVELED UP TO LEVEL 3! (Stats - HP: 20 (+10), Intelligence: 300 (+200)) You have now advanced to the Room 645. \
CAUTION: Some of the quizzes here can kill you in one shot. Your task now is to find Chris and give him the chocolates.
    {'Is the dress blue/black or white/gold?': 8, 'Are hot dogs sandwiches?': 16, 'Why are pizza boxes square but \
pizzas are circular?': 12, 'Is the opposite of opposite the same or opposite': 8}
    """
    player["level"] += 1
    player["HP"] += 10
    player["intelligence"] += 200
    player["location"] = "room_645"
    player["position"] = [1, 2]
    print(
        f"YOU LEVELED UP TO LEVEL 3! (Stats - HP: {player["HP"]} (+10), Intelligence: {player["intelligence"]} (+200"
        f")) You have now advanced to the Room 645. CAUTION: Some of the quizzes here can kill you in one shot. Your "
        f"task now is to find Chris and give him the chocolates.")
    return {each_question: value * 2 for each_question, value in surprise_questions.items()}


def level_up_to_2(player, surprise_questions):
    """
    Sets up the game for when character advances to level 2.

    :param player: a dictionary representing the character created for this game
    :param surprise_questions: a dictionary of surprise pop quiz questions
    :precondition: player and surprise_questions are provided in the correct format
    :precondition: player must be at level 1 and have 5 chocolates
    :precondition: character has greater than 0 HP
    :postcondition: increase player level by 1, HP by 10
    :postcondition: set location to student_lounge with a list of chocolate coordinates tuples and position to [3, 1]
    :postcondition: double the damage for each question
    :return: the list of chocolate coordinates associated with the location

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 100, 'HP': 10, 'position': [3, 1], \
'location': 'student_lounge', 'chocolate': 5}
    >>> questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4, \
"Why are pizza boxes square but pizzas are circular?": 3, "Is the opposite of opposite the same or opposite": 2}
    >>> level_up_to_2(character, questions)
    YOU LEVELED UP TO LEVEL 2! (Stats - HP: 20 (+10), Intelligence: 200 (+100)) You have now advanced to the \
Student Lounge. Be careful, the quizzes now deal twice the damage!
    {'Is the dress blue/black or white/gold?': 4, 'Are hot dogs sandwiches?': 8, 'Why are pizza boxes square but\
 pizzas are circular?': 6, 'Is the opposite of opposite the same or opposite': 4}
    """
    player["level"] += 1
    player["HP"] += 10
    player["intelligence"] += 100
    player["location"] = "student_lounge"
    player["position"] = [3, 1]
    print(
        f"YOU LEVELED UP TO LEVEL 2! (Stats - HP: {player["HP"]} (+10), Intelligence: "
        f"{player["intelligence"]} (+100)) You have now advanced to the Student Lounge. Be careful, "
        f"the quizzes now deal twice the damage!")
    return {each_question: value * 2 for each_question, value in surprise_questions.items()}


def pick_up_chocolate(player, area_description):
    """
    Pick up a chocolate at the character's position.

    :param player: a dictionary representing the character created for this game
    :param area_description: a list of tuples representing the coordinates of chocolates on the map
    :precondition: player and chocolate_coordinates are provided in the correct format
    :precondition: character has greater than 0 HP
    :postcondition: remove the corresponding chocolate coordinate when player's position matches that coordinate
    :return: a list of tuples representing the coordinates of the remaining chocolates on the map

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 3], \
'location': 'tech_hub', 'chocolate': 0}
    >>> location = {'rows': 8, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), \
(5, 3), (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), \
(4, 0), (5, 0), (6, 0), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4), \
(0, 5), (0, 6), (6, 1), (6, 5), (6, 6)], 'Chris': None, 'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), \
(3, 5), (2, 5)]}
    >>> pick_up_chocolate(character, location)
    <BLANKLINE>
    You picked up a Reese's chocolate! You now have 1.
    <BLANKLINE>

    >>> chocolate_places = location["chocolate_coordinates"]
    >>> print(chocolate_places)
    [(2, 3), (1, 3), (3, 5), (2, 5)]


    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': \
    'tech_hub', 'chocolate': 0}
    >>> location = {'rows': 8, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), \
    (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0),\
     (4, 0), (5, 0), (6, 0), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), \
     (0, 4), (0, 5), (0, 6), (6, 1), (6, 5), (6, 6)], 'Chris': None, 'chocolate_coordinates': [(3, 3), (2, 3), (1, 3),\
      (3, 5), (2, 5)]}
    >>> pick_up_chocolate(character, location)

    >>> chocolate_places = location["chocolate_coordinates"]
    >>> print(chocolate_places)
    [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]
    """
    if tuple(player["position"]) in area_description["chocolate_coordinates"]:
        player["chocolate"] += 1
        print(f"\nYou picked up a Reese's chocolate! You now have {player['chocolate']}.\n")
        area_description["chocolate_coordinates"].remove(tuple(player["position"]))


def is_alive(player):
    """
    Checks if the character is alive based on its HP points.

    :param player: a dictionary representing the character created for this game
    :precondition: player is provided in the correct format
    :postcondition: correctly checks if the character is alive with HP greater than 0 and False otherwise
    :return: a boolean - True if the HP is greater than zero and False otherwise

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location':\
'tech_hub', 'chocolate': 0}
    >>> is_alive(character)
    True

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 0, 'position': [3, 1], 'location': \
'tech_hub', 'chocolate': 0}
    >>> is_alive(character)
    You wake up from a nightmare
    False

    """
    if player["HP"] > 0:
        return True
    else:
        print("You wake up from a nightmare")
        return False


def update_hp_based_on_intelligence_for_final_exam(player):
    """
    Adjusts player health points based on intelligence points.

    :param player: a dictionary representing the character created for this game
    :precondition: player are provided in the correct format
    :precondition: character has greater than 0 HP
    :precondition: character location must room 645 and position is (6, 1)
    :postcondition: updates HP to 3 if player intelligence is equal or greater than 1000, 2 HP for 500, and 1 HP for
        less than 500

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': \
'tech_hub', 'chocolate': 0}
    >>> update_hp_based_on_intelligence_for_final_exam(character)
    >>> character['HP']
    1

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 749, 'HP': 10, 'position': [3, 1], 'location': \
'tech_hub', 'chocolate': 0}
    >>> update_hp_based_on_intelligence_for_final_exam(character)
    >>> character['HP']
    2
    """
    if player['intelligence'] >= 1000:
        player['HP'] = 3
    elif player['intelligence'] >= 500:
        player['HP'] = 2
    else:
        player['HP'] = 1


def final_exam_intro(player):
    """
    Prints the introduction for the final challenge for 'Pass COMP1510'.

    :param player: a dictionary representing the character created for this game
    :precondition: player is provided in the correct format
    :precondition: character has greater than 0 HP
    :precondition: character location must room 645 and position is (6, 1)
    :postcondition: correctly prints the introduction for the final challenge for 'Pass COMP1510'

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [6, 1], 'location': \
'room_645', 'chocolate': 0}
    >>> final_exam_intro(character)
    MWAHAHAHAHAHA
    Welcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your intelligence, I will grant \
you 1 tries.

    >>> character = {'name': 'Irene', 'level': 1, 'intelligence': 501, 'HP': 10, 'position': [6, 1], 'location': \
'room_645', 'chocolate': 0}
    >>> final_exam_intro(character)
    MWAHAHAHAHAHA
    Welcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your intelligence, I will grant you \
2 tries.
    """
    update_hp_based_on_intelligence_for_final_exam(player)
    repeated_ha = itertools.repeat('HA', 5)
    repeated_ha_string = ''.join(repeated_ha)
    print(
        f"MWA{repeated_ha_string}\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on \
your intelligence, I will grant you {player['HP']} tries.")


def final_exam(player):
    """
    Runs the final challenge for 'Pass COMP1510'.

    :param player: a dictionary representing the character created for this game
    :precondition: player is provided in the correct format
    :precondition: character has greater than 0 HP
    :precondition: character location must room 645 and position is (6, 1)
    :postcondition: correctly checks if the character passed the final exam
    :return: a boolean - True if the character passed the final exam 
    """
    questions = {"\nWhat is my favourite chocolate?\n[1]KitKat\n[2]Snickers\n[3]Reese's chocolate\n[4]Toblerone\n": '3',
                 "Does pineapple belong on my pizza?\n[1]It's not my first pick\n[2]Pineapple on pizza is *chef's "
                 "kiss*\n[3]Food sounds good to me\n[4]That's an abomination!\n": '4',
                 "Are you going to pass my course?\n[1]Yes\n[2]No\n[3]I forgot to mention I have Reese's chocolates!\n"
                 "[4]PLEASE\n": "3"}

    correct_answer_count = 0
    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer == answer:
            print("I see that you pay attention in class. Very good!\n")
            correct_answer_count += 1
            if correct_answer_count == 3:
                print("Congratulations!")
                return True
        else:
            player['HP'] -= 1
            print("Oof, not quite. But nice try.")
            if player['HP'] == 0:
                break


def game():
    """
    Run the game
    """
    player_name = welcome_message()
    character = make_character(player_name)
    maps_with_boundaries = initialize_map(character)
    current_location = give_location_description(character, maps_with_boundaries)
    quiz_attacks = make_quiz_questions()
    print_map(character, current_location)
    passed_comp1510 = False
    while is_alive(character) and not passed_comp1510:
        direction = get_user_choice()
        valid_move = validate_move(character, current_location, direction)
        if valid_move:
            move_character(character, direction)
            pick_up_chocolate(character, current_location)
            if quiz_probability():
                surprise_pop_quiz(character, quiz_attacks)
            if character['chocolate'] == 5 and character['level'] == 1:
                quiz_attacks = level_up_to_2(character, quiz_attacks)
            elif character['chocolate'] == 10 and character['level'] == 2:
                quiz_attacks = level_up_to_3(character, quiz_attacks)
            current_location = give_location_description(character, maps_with_boundaries)
            print_map(character, current_location)
            if character["position"] == [6, 1] and character["location"] == "room_645":
                final_exam_intro(character)
                passed_comp1510 = final_exam(character)
        else:
            print("\nYou can't go there!")


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
