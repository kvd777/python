# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Kane van Doorn
"""
__version__ = 8

# 2) print_introduction: Print a friendly welcome message for your game
def print_introduction():
    # print the introduction including the setting and some story.
    
    print("You're riding your horse when you hear a scream coming from a dark and looming tower in the distance")
    print("You think back to a few weeks ago.")
    print("You overheard some men at the local brothel talking about a missing princess.")
    print("You decide to take this as an opportunity to prove yourself to your guild.")
    print("You approach the tower and dismount your horse.")
    print("\nYou notice alligators are lurking in the water.")
    
# 3) get_initial_state: Create the starting player state dictionary

def get_initial_state():
    # Start the player states for the beginning of the game
    
    initial_states = {'game status': 'playing',
                      'location': 'The moat in front of the Tower',
                      'Sword': False,
                      'Crown': False
                      }
    return initial_states

# 4) print_current_state: Print some text describing the current game world

def print_current_state(a_dict):
    # Current location in the world, updates as the player chooses options and moves through the world.
    
    print("\nCurrent Location: "+ a_dict['location'] + ".")

# 5) get_options: Return a list of commands available to the player right now

def get_options(the_player):
    # Returns a list of options depending on where the player is in the world.
    
    if the_player['location'] == 'The moat in front of the Tower':
        a_list = ['Take the sword out of the rock, kill the alligators.',
                  'Attack the alligators with your fists.'
                  ]
    if the_player['location'] == 'Top of the Tower':
        a_list = ['Knock on the door.',
                  'Use the sword to silently pick the lock.'
                  ]
    if the_player['location'] == 'Inside the bedroom':
        a_list = ['Steal the crown.',
                  'Untie and save the princess.'
                  ]                  
    return a_list

# 6) print_options: Print out the list of commands available    

def print_options(a_list):
    # Prints the options from get_options()
    
        print('Your options are:')
        for x in a_list:
            print(x)        

# 7) get_user_input: Repeatedly prompt the user to choose a valid command

def get_user_input(a_list):
    # While loop that will ask the user for input until a valid option is chosen or quit is chosen.
    
    command = ""
    a = True
    while a == True:
        command = input('What would you like to do: ')
        if command in a_list:
            a = False
        if command.lower() == 'quit':
            a = False            
    return command 

    
# 8) process_command: Change the player state dictionary based on the command

def process_command(a_command, a_player):
    # Process the command, this involves updating if the sword and crown have been picked up based off of what options are chosen.
    
    if a_command == 'Take the sword out of the rock, kill the alligators.':
        a_player['location'] = 'Top of the Tower'
        a_player['Sword'] = True
    if a_command == 'Attack the alligators with your fists.':
        a_player['location'] = 'Bottom of the moat'
        a_player['game status'] = 'lose'
    if a_command == 'Knock on the door.':
        a_player['location'] = 'Bottom of the moat'
        a_player['game status'] = 'lose'
    if a_command == 'Use the sword to silently pick the lock.':
        a_player['location'] = 'Inside the bedroom'
    if a_command == 'Untie and save the princess.':
        a_player['location'] = 'Inside the bedroom'
        a_player['game status'] = 'lose'
    if a_command == 'Steal the crown.':
        a_player['location'] = 'Outside the tower'
        a_player['game status'] = 'win'
    if a_command.lower() == 'quit':
        a_player['game status'] = 'quit'

# 9) print_game_ending: Print a victory, lose, or quit message at the end    
     
def print_game_ending(a_player):
    # Prints an ending based off if the player chooses a losing option, winning option, or inputs quit.
    
    if a_player['location'] == 'Bottom of the moat' and a_player['game status'] == 'lose':
        print('You lost. The alligators ate you and you died. :(')
    if a_player['location'] == 'Bottom of the moat' and a_player['game status'] == 'lose':
        print('You lost. The evil witch heard you knocking and she killed you. :(')
    if a_player['location'] == 'Inside the bedroom' and a_player['game status'] == 'lose':
        print('You lost. Why would you save the princess if you could steal her crown? You are in a thiefs guild, STEAL THE CROWN')
    if a_player['location'] == 'Outside the tower' and a_player['game status'] == 'win':
        print('YOU WIN. You bring the crown back to the guild and sell it for a bag of gold.')
    if a_player['game status'] == 'quit':
        print('You quit the game. Goodbye!')
    else:
        print('Invalid Journey')
     
# Command Paths to give to the unit tester
WIN_PATH = ['Take the sword out of the rock, kill the alligators.', 'Use the sword to silently pick the lock.', 'Steal the crown.']
LOSE_PATH = ['Take the sword out of the rock, kill the alligators.', 'Use the sword to silently pick the lock.', 'Untie and save the princess.']

# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)

# Executes the main function
if __name__ == "__main__":
    '''
    You might comment out the main function and call each function
    one at a time below to try them out yourself '''
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # print_introduction()
    # print(get_initial_state())
    # ...