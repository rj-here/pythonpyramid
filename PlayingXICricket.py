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
    role = input(f'Enter the role of {player} (batter, bowler, all-rounder, wicket-keeper): ')
    #To check if the role is valid
    valid_roles = ['batter', 'Batter', 'BATTER', 'bowler', 'Bowler', 'BOWLER', 'allrounder', 'Allrounder', 'ALLROUNDER', 'bowling allrounder', 'Bowling Allrounder', 'BOWLING ALLROUNDER', 'batting allrounder', 'Batting Allrounder', 'BATTING ALLROUNDER', 'wicketkeeper', 'Wicketkeeper', 'WICKETKEEPER']
    if role not in valid_roles:
        print(f'Invalid role! Please enter a valid one for {player}')
        role = input(f'Enter the role of {player}')
    
    else:
        print(f'Adding {player} as {role} to the playing XI.')
        my_playing_XI[player] = role + ', ' #Updating player's role in the dictionary!
#Now, to define the captain, vice-captain
captain = input('Enter the name of the captain: ') #For the captain
if captain not in my_playing_XI:
    print(f'{captain} is not in the playing XI! Please enter a valid captain.')
    captain = input('Enter the name of the captain: ')
else:
    print(f'{captain} is set as the captain of the playing XI.')

viceCaptain = input('Enter the name of the vice-captain: ') #For the vice-captain
if viceCaptain not in my_playing_XI:
    print(f'{viceCaptain} is not in the playing XI! Please enter a valid vice-captain.')
    viceCaptain = input('Enter the name of the vice-captain: ')
elif viceCaptain == captain:
    print(f'{viceCaptain} is already the captain! Enter their name of their deupty!')
    viceCaptain = input('Enter the name of the vice-captain: ')
else:
    print(f'{viceCaptain} is set as the vice-captain of the playing XI.')

#Now, we will identify the types (right or left-handed, spin or seam, etc)
for player in my_playing_XI:
    #First, type of batter (while bowlers are not expected to bat much, in the case they do, they still either are a rightie or lefite!)
    batting_hand = input(f'Is {player} a right-handed or left-handed batter? Enter R for right-handed, L for left-handed:')
    if player not in ['wicket-keeper']:
        if batting_hand in ['R', 'r']:
            my_playing_XI[player] += 'right-handed batter, '
        elif batting_hand in ['L', 'l']:
            my_playing_XI[player] += 'left-handed batter, '
    else:
        if batting_hand in ['R', 'r']:
            my_playing_XI[player] += 'right-handed batter'
        elif batting_hand in ['L', 'l']:
            my_playing_XI[player] += 'left-handed batter'
    #Bowling details (asking for all except wicket-keeper, as even part-time they are not expected to bowl)
    if player not in ['wicket-keeper']:
        bowling_arm = input(f'Is {player} a right-arm or left-arm bowler? Enter R for right-arm, L for left-arm:') #Take the arm (right or left)
        bowling_type = input(f'Is {player} a spin or seam bowler? Enter spin for spin, seam for seam: ')
        #For Spin - references: https://en.wikipedia.org/wiki/Spin_bowling | https://en.wikipedia.org/wiki/Left-arm_orthodox_spin | https://en.wikipedia.org/wiki/Left-arm_unorthodox_spin
        if bowling_type in ['Spin', 'spin', 'SPIN']:
            spin_type = input(f'What type of spinner is {player}? Enter L for leg-spin (for right armers, OR for lefties: left-arm unorthodox spin). Enter O for off-spin (for right armers, OR for righties: left-arm orthodox spin)')
            if spin_type in ['L', 'l']:
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm leg-spinner'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm leg-spinner'
            elif spin_type in ['O', 'o']:
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm off-spinner'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm off-spinner'
        #For Seam - references: https://en.wikipedia.org/wiki/Types_of_bowlers_in_cricket 
        elif bowling_type in['Seam', 'seam', 'SEAM']:
            seam_type = input(f'Is {player} a fast, fast-medium, medium-fast, medium, or slow bowler? Enter 1 for fast, 2 for fast-medium, 3 for medium-fast, 4 for medium, 5 for medium-slow, 6 for slow-medium, 7 for slow:')
            if seam_type == '1':
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm fast bowler'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm fast bowler'
            elif seam_type == '2':
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm fast-medium bowler'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm fast-medium bowler'
            elif seam_type == '3':
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm medium-fast bowler'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm medium-fast bowler'
            elif seam_type == '4':
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm medium bowler'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm medium bowler'
            elif seam_type == '5':
                if bowling_arm in ['R', 'r']:
                    my_playing_XI[player] += 'right-arm slow bowler'
                elif bowling_arm in ['L', 'l']:
                    my_playing_XI[player] += 'left-arm slow bowler'
print('Your playing XI is ready!')
for player, role in my_playing_XI.items():
    if (player == captain):
        print(f'{player} ({role}, c)')
    elif (player == viceCaptain):
        print(f'{player} ({role}, vc)')
    else:
        print(f'{player} ({role})')
    


#© 2025 Rishi
#Last updated: 23rd July, 2025