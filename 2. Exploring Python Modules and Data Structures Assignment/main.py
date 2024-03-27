# Objective:
# The aim of this assignment is to deepen your understanding of Python modules, 
# both built-in and custom, and to enhance your skills in working with various 
# Python data structures like lists, dictionaries, and sets. This assignment focuses 
# on practical applications of these concepts in real-world scenarios.

# Task 1: Contact List Manager

#     Problem Statement: Create a Python script using a custom module to manage a 
# contact list. The script should allow adding, removing, and displaying contacts stored in a list.

#     Code Example:

#     # contacts_manager.py
#     # Define functions to add, remove, and display contacts

#     # main.py
#     # Implement the logic to interact with the contact manager

import contacts_manager

def main():
    while True:

        print("\nPlease make a selection from the following menu:\n1 - Add a new contact\n2 - Edit an existing contact\n3 - Delete a contact\n4 - Search for a contact\n5 - Display all contacts\n6 - Export contacts to a text file\n7 - Import contacts from a text file\n8 - Quit")
        try:
            command = int(input("\nEnter the number of the command you would like to select\n").strip())
        except:
            print("Please ensure you make a valid selection!\n")
        else:
            if command > 0 and command <= 8:
                commandStr = str(command)
               
                if commandStr == "1":
                    #1. Add a contact
                    print("Ok lets add a new contact to your contacts list!")
                    email = input("What's your new contact's email address?").strip()
                    
                    contacts_manager.addContact(email)
                    
                if commandStr == "2":
                    #2. Edit an existing contact
                    print("\nOk, lets delete a contact")
                    name = input("Enter the name of the contact you'd like to edit:\n").strip()
                    contacts_manager.editContact(name)

                if commandStr == "3":
                    #3. Delete a contact
                    print("\nOk, lets delete a contact")
                    name = input("Enter the name of the contact you'd like to delete:\n").strip()
                    contacts_manager.delContact(name)
                    
                if commandStr == "4":
                    #4. Search for a contact
                    print(f"\nOk let's find a contact...")
                    name = input("What's the name of the person you're looking for:")
                    contacts_manager.searchContact(name)
                    
                if commandStr == "5":
                    #5. Display all contacts
                    contacts_manager.dispContacts()

                if commandStr == "6":
                    #6. Export contacts to a text file
                    contacts_manager.exportContact()
                    
                if commandStr == "7":
                    #7. Import contacts from a text file
                    contacts_manager.importContact()
                    
                if commandStr == "8":
                    #8. Quit
                    print("\nYou selected 8!")
                    print("Thanks for using the Contact Management Service!")
                    break
            else:
                print("Make sure you enter a number between 1 and 8!")

main()

#     Expected Outcome: Your script should be able to add new contacts, remove existing 
# contacts, and display all contacts. Each contact can be a dictionary with a name and phone number.

# Task 2: Date Extractor


#     Problem Statement: Write a Python program that uses the datetime module to extract 
# and display the current month and year. Additionally, allow the user to input a date string 
# and parse it into a datetime object.

#     Code Example:

#     # main.py
#     from datetime import datetime
#     # Implement code to display the current month and year
#     # Implement code to parse a user-input date string into a datetime object

#     Expected Outcome: The program should accurately display the current month and year
# and successfully convert a user-input date string (e.g., "2023-03-15") into a datetime 
# object, handling any invalid inputs gracefully.

import datetime
import re


currentDate = datetime.date.today()

print(f"The current date is {currentDate}")
date = []
user = input("What date would you like to convert to a datetime object? (Please retain order YYYY MM DD regardless of what you enter or whats in between)").strip()



matches = list(re.finditer(r"\b(\d{4}).{1,}(\d{2}).{1,}(\d{2})\b", user))

if matches:
    for match in matches:
        year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
        print(f"the entered data was: {datetime.datetime(year, month, day)}")
else:
    print("Sorry, I couldn't find a valid date in that string!")