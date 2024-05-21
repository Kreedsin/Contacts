import colorama #Introduced and added colourama to text throughout code to make it look neat and tidy
from colorama import Fore, Style, init

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        
# contacts we already have. & additions
class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact(Fore.LIGHTBLUE_EX + "Alice", "1234567890", "alice@email.com"+ Style.RESET_ALL),
            Contact(Fore.LIGHTBLUE_EX + "Bob", "9876543210", "bob@email.com"+ Style.RESET_ALL),
            Contact(Fore.LIGHTBLUE_EX + "Sue", "2870543890", "sue@email.com"+ Style.RESET_ALL),
            Contact(Fore.LIGHTBLUE_EX + "Dave", "5452165674", "dave@email.com"+ Style.RESET_ALL),
            Contact(Fore.LIGHTBLUE_EX + "Pete", "9875543890", "bob@email.com"+ Style.RESET_ALL),
        
        ]
#this funtion will add a new contact.
    def add_contact(self, name, phone_number, email):
        for contact in self.contacts:
            if contact.phone_number == phone_number: #Used chatGPT to find the right order, we had the right idea just in the wrong order. (we were trying to check in Contactbook / contacts)
                print(Fore.RED + "That number already exists" + Style.RESET_ALL)
                return #We were trying to use a break function at first, asked chatGPT why it wasn't working, got fix.
        for contact in self.contacts:
            if contact.email == email:
                print(Fore.RED + "That email already exists." + Style.RESET_ALL)
                return
        self.contacts.append (Contact(name, phone_number, email)) #Katy gave us a nudge in the right direction with this one, and how it interacts with the list of options.
        print(Fore.GREEN + f"Contact '{name}' added successfully."+ Style.RESET_ALL)

#this function will update you someones detals when needed.
    def update_contact(self, name):
        for contact in self.contacts:
            contact_name_stripped = contact.name.replace(Fore.LIGHTBLUE_EX, "").replace(Style.RESET_ALL, "").lower()
            if contact_name_stripped == name:
                new_phone_number = input(Fore.LIGHTBLUE_EX +"Enter a new phone number: "+ Style.RESET_ALL)
                new_email = input(Fore.LIGHTBLUE_EX +"Enter a new email: "+ Style.RESET_ALL)

                if new_phone_number:
                    contact.phone_number = new_phone_number #Allows phone number to be overwritten
                if new_email:
                    contact.email = new_email #Allows email to be overwritten
                print(Fore.GREEN+f"Contact {name} was updated successfully."+ Style.RESET_ALL)
                return
        print(Fore.RED + f"Contact {name} was not found." + Style.RESET_ALL)
                
#this function will show all contacts. 
    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")         
        for contact in self.contacts: #Using a for loop to display all contacts
            print(Fore.LIGHTYELLOW_EX +f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n"+ Style.RESET_ALL)
        else:
            print(Fore.RED + "No more contacts found." + Style.RESET_ALL)
            
    
#this function searchers for a contact. 
    def Search_all_contacts(self, name):
        for contact in self.contacts:
            contact_name_stripped = contact.name.replace(Fore.LIGHTBLUE_EX, "").replace(Style.RESET_ALL, "").lower() #Used chatGPT to get this line of code so that it would take out the colorama from our print statement otherwise the code would try to run the Fore and wouldn't work
            if contact_name_stripped == name:
                print (Fore.LIGHTBLUE_EX + f"Contacts name: {contact.name}, contacts phone number: {contact.phone_number}, contacts email: {contact.email}."+ Style.RESET_ALL)
                return 
        print(Fore.RED + f"Contact '{name}' was not found." + Style.RESET_ALL)


# this function deletes a contact
    def delete_a_contact(self, name):
        for contact in self.contacts:
            contact_name_stripped = contact.name.replace(Fore.LIGHTBLUE_EX, "").replace(Style.RESET_ALL, "").lower()
            if contact_name_stripped == name:
                self.contacts.remove(contact) #If the entered name matches will remove the contact
                print(Fore.GREEN + f"This Contact '{name}' is now deleted!" + Style.RESET_ALL)
                return
        print(Fore.RED + f"This Contact '{name}' was not found" + Style.RESET_ALL)


#reverses the order of the contact list
    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: contact.name.lower()) #chatgpt we didnt know that lambda was a thing.. but it sorts lists in to order.. 
        print(Fore.LIGHTYELLOW_EX + "Contacts sorted in order:"+ Style.RESET_ALL)
        for contact in self.contacts:
                print(Fore.LIGHTYELLOW_EX +f"Name: {contact.name}\n Phone: {contact.phone_number}\n Email: {contact.email}\n"+ Style.RESET_ALL)
        

    def reverse_contacts(self): #For fun we decided to add an option that can show contacts in reversed order
        self.contacts.sort(key=lambda contact: contact.name.lower(), reverse=True) #chatgpt to show where the reverse function goes 
        print(Fore.LIGHTYELLOW_EX + "Contacts sorted in order:"+ Style.RESET_ALL)
        for contact in self.contacts:
            print(Fore.LIGHTYELLOW_EX +f"Name: {contact.name}\n Phone: {contact.phone_number}\n Email: {contact.email}\n"+ Style.RESET_ALL)


 
  # user interface....   
def main():
    contact_book = ContactBook()

    while True:
        print(Fore.LIGHTGREEN_EX + "\n--- Contact Book Menu ---" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "1. Add new contact")
        print("2. Update a current contact")
        print("3. Display all contacts")
        print("4. Search for a contact")
        print("5. Delete a contact")
        print("6. Contacts in order")
        print("7. Reversed order contacts")
        print("0. Exit" + Style.RESET_ALL)

        choice = input(Fore.LIGHTGREEN_EX + "Enter your choice: " + Style.RESET_ALL)
# All Questions for user>
        if choice == "1":
            print("________________________________________________________________")
            name = input(Fore.LIGHTYELLOW_EX + "Enter name: "+ Style.RESET_ALL)
            phone_number = input(Fore.LIGHTYELLOW_EX +"Enter phone number: "+ Style.RESET_ALL)
            email = input(Fore.LIGHTYELLOW_EX +"Enter email: "+ Style.RESET_ALL)
            contact_book.add_contact(name, phone_number, email) #connection to add contanct
        elif choice == "2":
            print("________________________________________________________________")
            name = input(Fore.LIGHTYELLOW_EX +"Enter the name of the contact you would like to update: "+ Style.RESET_ALL)
            contact_book.update_contact(name) #connection to update contact
        elif choice == "3": 
            print("________________________________________________________________")
            contact_book.display_all_contacts() #connection to display all contacts
        elif choice == "4":
            print("________________________________________________________________")
            name = input(Fore.LIGHTYELLOW_EX +"Enter the name of the contact you would like to search: "+ Style.RESET_ALL).lower()
            contact_book.Search_all_contacts(name) #connection to search all contacts
        elif choice == "5":
            print("________________________________________________________________")
            name = input(Fore.LIGHTYELLOW_EX +"please enter the name of the contact you wish to delete: " + Style.RESET_ALL)
            contact_book.delete_a_contact(name) #connection to delete a contacts
        elif choice == "6":
            print("________________________________________________________________")
            name = print(Fore.LIGHTYELLOW_EX +"sorted all contacts A to Z  " + Style.RESET_ALL)
            contact_book.sort_contacts() #connection to sort all contacts
        elif choice == "7":
            print("________________________________________________________________")
            name = print(Fore.LIGHTYELLOW_EX +"sorted all contacts Z to A  " + Style.RESET_ALL)
            contact_book.reverse_contacts() #connection to reverse all contacts
        elif choice == "0":
            print("________________________________________________________________")
            print(Fore.GREEN + "Exiting Contact Book. Goodbye!" + Style.RESET_ALL)
            break
            
        else:
            print(Fore.RED +"Incorrect information provided, please try again."+ Style.RESET_ALL)
            

if __name__ == "__main__":
    main()