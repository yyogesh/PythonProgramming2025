from contacts import *
from validation import *

def display_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Display All Contacts")
    print("5. Exit")


def add_new_contact():
    name = input("Enter name: ")
    while True:
        phone = input("Enter phone number: ")
        if validate_phone(phone):
            phone = format_phone(phone)
            break
        print("Invalid phone number. Please try again.")
    
    while True:
        email = input("Enter email: ")
        if validate_email(email):
            break
        print("Invalid email address. Please try again.")

    contact = add_contact(name, phone, email)
    print("Contact added successfully:", contact)

def search_contact():
    term = input("Enter search term (name or phone): ").strip()
    results = find_contact(term)
    if results:
        print("Search results:")
        for contact in results:
            print(f"ID: {contact['id']}, Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No matching contacts found.")

def update_Existing_contact():
    contact_id = int(input("Enter contact ID to update: "))
    
    contact = None
    
    for c in contacts:
        if c['id'] == contact_id:
            contact = c
            break
    
    if not contact:
        print("Contact not found.")
        return
    
    print(f"\nUpdating contact: {contact['name']}")
    name = input(f"Name ({contact['name']}): ").strip()
    phone = input(f"Phone ({contact['phone']}): ").strip()
    email = input(f"Email ({contact['email']}): ").strip()

    if not name: name = None
    if not phone: phone = None
    if not email: email = None

    update_contact(contact_id, name, phone, email)
    print("Contact updated successfully.")

def show_all_contacts():
    all_contacts = list_all_contacts()
    if all_contacts:
        print("\nAll Contacts:")
        for contact in all_contacts:
            print(f"{contact['id']}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts available.")

def main():
    add_contact("John Doe", "123-456-7890", "2H2m0@example.com")
    add_contact("Jane Doe", "987-654-3210", "2H2m0@example.com")
    add_contact("John Smith", "555-555-5555", "2H2m0@example.com")
    add_contact("Jane Smith", "111-111-1111", "2H2m0@example.com")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
           add_new_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_Existing_contact()
        elif choice == "4":
            show_all_contacts()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()