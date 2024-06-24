contacts = {}

def display_contacts():
    print("Name\t\tContact Number")
    if contacts:
        for name, number in contacts.items():
            print(f"{name}\t\t{number}")
    else:
        print("No contacts found.")

def add_contact():
    name = input("Enter the name: ")
    number = input("Enter the mobile number: ")
    contacts[name] = number
    print("Contact added successfully.")

def search_contact():
    search_name = input("Enter the contact name to search: ")
    if search_name in contacts:
        print(f"{search_name}'s contact number is {contacts[search_name]}.")
    else:
        print("Name not found in contacts.")

def update_contact():
    update_name = input("Enter the contact name to update: ")
    if update_name in contacts:
        new_number = input("Enter the new mobile number: ")
        contacts[update_name] = new_number
        print("Contact updated successfully.")
    else:
        print("Name not found in contacts.")

def delete_contact():
    delete_name = input("Enter the contact name to delete: ")
    if delete_name in contacts:
        confirm = input(f"Do you want to delete {delete_name}? (yes/no): ")
        if confirm.lower() == 'yes':
            del contacts[delete_name]
            print("Contact deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Name not found in contacts.")

if __name__ == "__main__":
    print("Welcome to the Contact Management System!")
    
    while True:
        print("\nMenu:")
        print("1. Add new Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                add_contact()
            
            elif choice == 2:
                display_contacts()
            
            elif choice == 3:
                search_contact()
            
            elif choice == 4:
                update_contact()
            
            elif choice == 5:
                delete_contact()
            
            elif choice == 6:
                print("Exiting the program...")
                break
            
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
