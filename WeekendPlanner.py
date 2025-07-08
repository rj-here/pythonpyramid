#This program will be to help you plan a weekend. This would incorporate various categories, in try to give you a brief overview of your plans
#This is a basic program to help you list out your thoughts, and can use this guide your plans. I currently don't intend to expand this, but I will not rule out future considerations.
#This is part of a growing collection of Python programs, for me to get a proper grasp of basics, and for you to see.
print('Hello there! This will be a weekend planner. This is going to be more focused on a general across tasks I have or observe people having on the weekend.')

def whatHouseTasks():
    print('What house related tasks do you need to complete? Seperate them with |')
    houseTasks = input('House tasks: ') #inputting the house tasks
    houseTasksList = houseTasks.split(' | ')
    print('House tasks: ')
    print('One-by-one:')
    for task in houseTasksList: #printing each one by one
        print(task)
    print('So, your house tasks for the weekend are: ') #printing them all, seeing how printing a list goes
    print(houseTasksList)

whatHouseTasks()

def whatOccasionalTasks():
    print('What occasional tasks (getting a haircut, cutting the grass, etc) do you need to complete? Seperate with them |')
    occasionalTasks = input('Occasional tasks: ') #inputting the occasional tasks
    occasionalTasksList = occasionalTasks.split(' | ')
    print('Occasional tasks: ')
    print('One-by-one:')
    for task in occasionalTasksList: #printing each one by one
        print(task)
    print('So, your occasional tasks for the weekend are: ') #printing them all, seeing how printing a list goes
    print(occasionalTasksList)

whatOccasionalTasks()

def whatSpecialThings():
    print("What special things (go out for dinner, watch a movie, etc) would you like to do? Seperate them with |")
    specialThings = input('Special things: ') #inputting the special things
    specialThingsList = specialThings.split(' | ')
    print('Special things: ')
    print('One-by-one:')
    for task in specialThingsList: #printing each one by one
        print(task)
    print('So, the special things, hopefully making your weekend a little more special are: ') #printing them all, seeing how printing a list goes
    print(specialThingsList)

whatSpecialThings()

#© 2025 Rishi
#Last updated: 8th July, 2025