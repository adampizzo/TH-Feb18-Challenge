#For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
#Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
#Try to make sure that the program doesn't crash at any point!
#As an extra challenge, make the program continue to run until the user decides to quit.

import os
import sys
import time


class PersonNotInDatabaseError(Exception):
    pass


class MenuSelectionError(Exception):
    pass


user_dictionary = [{
        'name': 'joe schmoe',
        'birthday': '01/05/1698'        
    },
    {
        'name': 'jane smith',
        'birthday': '09/24/2005'
    },
    {
        'name': 'peggy sue',
        'birthday': '04/02/1986'
    },
    {
        'name': 'uncle sam',
        'birthday': '07/04/1776'
    }                          
]

def clear():
    ''' The purpose of the clear function is to determine what the operating system and then clear the screen.'''    
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


#Get Name of user to look up
def get_name(dictionary):
    while True:
        try:
            name = input("\nWhose birthday do you want to look up?\n")
            matching_users = []
            for users in dictionary:
                if users['name'] == name.lower():
                    matching_users.append(users['name'])
            if len(matching_users) == 0:
                raise PersonNotInDatabaseError(f"\n{name} is not a person in our database. Please try again.\n") 
        except PersonNotInDatabaseError as err:
            print(err)                    
        else:
            return(name.lower())
                            
            
#return Birthday
def return_birthday(name, dictionary):    
    for user in dictionary:
        if user['name'] == name:                
            return user['birthday']
        
        
#Get Dictionary         
def print_current_dictionary(dictionary):
    for users in dictionary:
        print(users['name'].title())
        time.sleep(.45)

#Check to see if the user wants to continue running the program
def keep_running():
    print("Do you want to run the program again?")
    print("1) Yes")
    print("2) No")
    while True:
        try:
            get_selection = input("Enter Selection: ")
            get_selection = int(get_selection)
            if get_selection != 1 and get_selection != 2:
                raise MenuSelectionError(f"{get_selection} is not a valid entry.\n")
        except ValueError:
            print(f"{get_selection} is not a valid entry.\n")
        except MenuSelectionError as err:
            print(err)
        else:
            if get_selection == 2:
                print("\nThank you for using the Birthday Dictionary!")
                time.sleep(1)
                return False
                break
            else:
                clear()
                return True
                break

#Run program until the use quits.
def run_program():
    running = True
    
    while running:
        print("Welcome to the Birthday Dictionary. We know the birthdays of:")
        print_current_dictionary(user_dictionary)
        time.sleep(1)
        user_choice = get_name(user_dictionary)
        time.sleep(1)
        print(f"\n{user_choice.title()}'s birthday is {return_birthday(user_choice, user_dictionary)}.\n")
        time.sleep(1)
        running = keep_running()
        
                
#Start Program
run_program()
        