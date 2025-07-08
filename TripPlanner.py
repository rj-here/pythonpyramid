#This program is supposed to help you plan a trip. This will feature many parts, and is partly inspired by my personal trip planning template.
#This is just a quick and basic way for you to note down your ideas, which you can then use to plan out further. I currently do not plan to expand this, but I may consider in the future.
#This is part of a growing collection of Python programs, for me to get a proper grasp of basics, and for you to see.
print('Welcome! This is going to be a trip planner, assisting in details like the location, activities, people accompanying, shopping list, and more.')
def typeOfTrip():
    tripType = input('What type of trip is being planned? (Day trip, weekend trip, week-long, or just a good old long proper vacation?)\n')
    print(f'This trip is a {tripType}.')

typeOfTrip()

def tripLocation():
    location = input('Where is the trip going to be?\n')
    print(f'The trip is at {location}.')

tripLocation()

def tripActivities():
    activities = input('What are the objectives of yours for the trip? Seperate them with | \n')
    print('The activities planned for the trip are:')
    for activity in activities.split(' | '):
        print({activity})

tripActivities()   

def tripCompany():
    print('Who is joining on you on the trip?')
    people = input('Input the people joining you, separated by | \n')
    peopleList = people.split(' | ')
    print(f'All these people are joining you on the trip: {peopleList}')

tripCompany()

def tripShoppingList():
    print('What do you plan to get while on the trip? I try and get something that makes me remember the trip, whether a magnet or a t-shirt \n')
    shopping = input('Input the items you plan to get, separated by | \n')
    shoppingList = shopping.split(' | ')
    print(f'You\'re planning to get: {shoppingList} during the trip')

tripShoppingList()

def tripBudget():
    budget = input('What\'s the rough budget for the trip? \n')
    print(f'The budget for the trip is: {budget}')
tripBudget()

#© 2025 Rishi
#Last updated: 8th July, 2025