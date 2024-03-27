import json

print("\nWelcome to the Contact Management System!")

contacts = {
    "janemansfield@gmail.com": {"name": "Jane Mansfield", "phone": "123-543-6432", "address": "34 Urban Parkway"},
    "bobdingle@hotmail.com": {"name": "Bob Dingle", "phone": "904-123-6516", "address": "99 Street Avenue"},
    "guyFieri@aol.ca": {"name": "Guy Fieri", "phone": "934-654-1253", "address": "100 Diner Street"}
}

def addContact(email):
    global contacts
    print("Ok, lets add a new contact for you!")

    name = input("\nWhat's your contacts name?\n").strip()
    phone= input("\nWhat's your contacts phone number?\n").strip()
    address= input("\nWhat's your contact's address?\n").strip()
    if email not in contacts:
        contacts[email] = {"name": name, "phone": phone, "address": address}
    else:
        print(f"Sorry, you already have a contact listed for the email address {email}")

    print(f"Awesome! Your new contact '{contacts[email]}' has been added!\n")
    dispContacts()


def editContact(name):
    global contacts
    foundContact = False

    for contact, info in contacts.items():
        for entry, value in info.items():
            if value.lower() == name.lower():
                editContact = contact
                foundContact = True
                break
    if foundContact:
        print(f"\nOk, what information would you like to change about {editContact}?")
        changeCategory = input("Please enter: email, name, address, phone - or leave blank to return to menu\n").strip()
        if changeCategory:        
            if changeCategory == "name":
                newName = input("\nWhat would you like to change the name to?\n").strip()
                contacts[editContact]["name"] = newName
                print(f"succesfully change the name of {editContact} to {newName}")
                
            elif changeCategory == "email":
                newEmail = input("\nWhat would you like to change the email to?\n").strip()
                contacts[newEmail] = contacts[editContact]
                print(f"succesfully change the email of {editContact} to {newEmail}")
                del contacts[editContact]
                
            elif changeCategory == "address":
                newAddress = input("\nWhat would you like to change the address to?\n").strip()
                contacts[editContact]["address"] = newAddress
                print(f"succesfully change the address of {editContact} to {newAddress}")

            elif changeCategory == "phone":
                newPhone = input("\nWhat would you like to change the phone number to?\n").strip()
                contacts[editContact]["phone"] = newPhone
                print(f"succesfully change the phone number of {editContact} to {newPhone}")

            else:
                print("Please make sure you make a valid selection from the menu!")
    else:
        print(f"Sorry, I couldn't find a contact named '{name}'")

def delContact(name):
    global contacts
    foundContact = False

    for contact, info in contacts.items():
        for entry, value in info.items():
            if value.lower() == name.lower():
                delContact = contact
                foundContact = True
                break
    if foundContact:
        print(f"removing {contacts[delContact]}")
        del contacts[delContact]
    else:
        print(f"Sorry, I couldn't find a contact named '{name}'")
    
def searchContact(name):
    RetrieveContact = ""

    for contact, info in contacts.items():
        for entry, value in info.items():
            if value.lower() == name.lower():
                RetrieveContact = contact 
                break
    if bool(RetrieveContact) == True:
        print(f"found '{name}':")
        print(f"  - {RetrieveContact}")
        for key, value in contacts[RetrieveContact].items():
            print(f"  - {value}")
    else:
        print(f"Sorry, I couldn't find a contact named '{name}'")

def dispContacts():
    print(f"\nHere are all your contacts:\n")

    for contact, info in contacts.items():
        print(f"{contact}:")
        for name, value in info.items():
            print(f"  - {value}")
            

def exportContact():
    print("Ok! Exporting your contacts to file...\n")
    with open("2. Exploring Python Modules and Data Structures Assignment/Files/Output/ContactsExports.txt", "w") as file:
        json.dump(contacts, file, indent=4)
        
        
def importContact():
    global contacts
    print("Ok! Importing contacts from file...\n")
    with open('2. Exploring Python Modules and Data Structures Assignment/Files/Input/contactsImport.txt', 'r') as file:
        newContacts = json.load(file)
        contacts.update(newContacts)
    print("\nHere is your updated Contact List:\n")
    dispContacts()

