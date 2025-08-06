#This is a program that lets you input the playing XI for a cricket match.
#This is part of a growing collection of Python programs, for me to get a proper grasp of basics, and for you to see.
print('Welcome! Here you can input your playing XI for a cricket match.')
my_playing_XI = {} #This will be a dictionary to hold player name, and role (batter, bowler, all-rounder). The captain & vice-captain will be assigned at a later point, as well as types (opening batter, spin bowler, etc).
while (len(my_playing_XI) < 11):
    #Your team will have 11 players.
    player_name = input('Enter the name of the player: ')
    my_playing_XI.update({player_name: ''}) #Add the player to the dictionary with an empty role.
for player in my_playing_XI:
    #The valid roles are defined
    valid_roles = ['batter', 'Batter', 'BATTER', 'bowler', 'Bowler', 'BOWLER', 'allrounder', 'Allrounder', 'ALLROUNDER', 'bowling allrounder', 'Bowling Allrounder', 'BOWLING ALLROUNDER', 'batting allrounder', 'Batting Allrounder', 'BATTING ALLROUNDER', 'wicketkeeper', 'Wicketkeeper', 'WICKETKEEPER']
    #Now, we will get the role(s) of each player
    role = input(f'Enter the role of {player} (batter, bowler, allrounder (including batting and bowling allrounders), wicketkeeper): ').lower() #Converted to lowercase for easier validation.
    #Now, to validate correctness of the role
    while role not in valid_roles:
        print(f'Invalid role! Please enter a valid one for {player}')
        role = input(f'Enter the role of {player}: ').lower() #Again, converted to lowercase for easier validation.
    print(f'Adding {player} as {role} to the playing XI.')
    my_playing_XI[player] = role #Updating player's role in the dictionary!

#Now, ensuring there is a wicketkeeper in the team
if 'wicketkeeper' not in my_playing_XI.values():
    print('Warning: No wicketkeeper found in the playing XI! Please ensure you have a wicketkeeper in your team.')
    wicketkeeper = input('Enter the name of the wicketkeeper: ')
    while wicketkeeper not in my_playing_XI:
        print(f'{wicketkeeper} is not in the playing XI! Please enter a valid wicketkeeper.')
        wicketkeeper = input('Enter the name of the wicketkeeper: ')
    my_playing_XI[wicketkeeper] = 'wicketkeeper'
    print(f'{wicketkeeper} has been added as the wicketkeeper of the playing XI.')

#Now, ensuring there are at least 4 bowling options (bowlers / allrounders) in the team

#Now, to define the captain, vice-captain
captain = input('Enter the name of the captain: ') #For the captain
while captain not in my_playing_XI:
    print(f'{captain} is not in the playing XI! Please enter a valid captain.')
    captain = input('Enter the name of the captain: ')

print(f'{captain} is set as the captain of the playing XI.')

viceCaptain = input('Enter the name of the vice-captain: ') #For the vice-captain
while viceCaptain not in my_playing_XI or viceCaptain == captain:
    if viceCaptain == captain:
        print(f'{viceCaptain} is not a valid vice-captain as they are the captain, please enter a valid one!')
        viceCaptain = input(f'Enter a valid vice-captain: ')
    else:
        print(f'{viceCaptain} is not a valid vice-captain, please enter a valid one!')
        viceCaptain = input(f'Enter a valid vice-captain: ')
    
print(f'{viceCaptain} is set as the vice-captain of the playing XI.')

print('Your playing XI is ready!')
for player, role in my_playing_XI.items():
    if (player == captain):
        print(f'{player} ({role}, c)') # for captain
    elif (player == viceCaptain):
        print(f'{player} ({role}, vc)') #for vice-captain
    else:
        print(f'{player} ({role})') # for others

#© 2025 Rishi
#Last updated: 6th August, 2025