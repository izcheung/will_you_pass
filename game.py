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

