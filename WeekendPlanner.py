#This program will be to help you plan a weekend. This would incorporate various categories, in try to give you a brief overview of your plans
print('Hello there! This will be a weekend planner. This is going to be more focused on a general across tasks I have or observe people having on the weekend.')

def whatHouseTasks():
    print('What house related tasks do you need to complete? Seperate them with |')
    houseTasks = 'Groceries | Laundry'
    houseTasksList = houseTasks.split(' | ')
    print('House tasks: ')
    print('One-by-one:')
    for task in houseTasksList: #printing each one by one
        print(task)
    print('All at once:') #printing them all, seeing how printing a list goes
    print(houseTasksList)

whatHouseTasks()

def whatOccasionalTasks():
    print('What occasional tasks (getting a haircut, cutting the grass, etc) do you need to complete? Seperate with them |')
    occasionalTasks = 'Get a haircut | Cut the grass'
    occasionalTasksList = occasionalTasks.split(' | ')
    print('Occasional tasks: ')
    print('One-by-one:')
    for task in occasionalTasksList: #printing each one by one
        print(task)
    print('All at once:') #printing them all, seeing how printing a list goes
    print(occasionalTasksList)

whatOccasionalTasks()

def whatSpecialThings():
    print("What special things (go out for dinner, watch a movie, etc) would you like to do? Seperate them with |")
    specialThings = 'Going out for dinner | Meeting friends'
    specialThingsList = specialThings.split(' | ')
    print('Special things: ')
    print('One-by-one:')
    for task in specialThingsList: #printing each one by one
        print(task)
    print('All at once:') #printing them all, seeing how printing a list goes
    print(specialThingsList)

whatSpecialThings()

#© 2025 Rishi
#Last updated: 2nd July, 2025