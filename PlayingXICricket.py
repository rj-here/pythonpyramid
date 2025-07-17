#This is a program that lets you input the playing XI for a cricket match.
#This is part of a growing collection of Python programs, for me to get a proper grasp of basics, and for you to see.
print('Welcome! Here you can input your playing XI for a cricket match.')
my_playing_XI = {} #This will be a dictionary to hold player name, and role (batter, bowler, all-rounder). The captain & vice-captain will be assigned at a later point, as well as types (opening batter, spin bowler, etc).
while (len(my_playing_XI) < 11):
    #Your team will have 11 players.
    player_name = input('Enter the name of the player: ')
    my_playing_XI.update({player_name: ''}) #Add the player to the dictionary with an empty role.
print(my_playing_XI) #Print the current playing XI.
for player in my_playing_XI:
    #Now, we will get the role(s) of each player
    role = input(f'Enter the role of {player} (batter, bowler, all-rounder): ')
    #To check if the role is valid
    valid_roles = ['batter', 'bowler', 'all-rounder']
    if role not in valid_roles:
        print(f'Invalid role! Please enter a valid one for {player}')
        role = input(f'Enter the role of {player}')
    else:
        print(f'Adding {player} as {role} to the playing XI.')
        my_playing_XI[player] = role #Updating player's role in the dictionary!
print('Your playing XI is ready!')
print(my_playing_XI)

#© 2025 Rishi
#Last updated: 17th July, 2025