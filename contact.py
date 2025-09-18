import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

# Search contact
def search_contact(contacts):
    keyword = input("Enter name or phone number to search: ")
    results = [c for c in contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]
    if results:
        for c in results:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}, Address: {c['address']}")
    else:
        print("❌ No contact found.")

# Update contact
def update_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to update: ")) - 1
    if 0 <= idx < len(contacts):
        c = contacts[idx]
        print("Leave blank to keep existing value.")
        c['name'] = input(f"Name ({c['name']}): ") or c['name']
        c['phone'] = input(f"Phone ({c['phone']}): ") or c['phone']
        c['email'] = input(f"Email ({c['email']}): ") or c['email']
        c['address'] = input(f"Address ({c['address']}): ") or c['address']
        save_contacts(contacts)
        print("✅ Contact updated successfully!")
    else:
        print("❌ Invalid contact number.")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        deleted = contacts.pop(idx)
        save_contacts(contacts)
        print(f"🗑 Deleted contact: {deleted['name']}")
    else:
        print("❌ Invalid contact number.")

# Main program
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Exiting Contact Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if _name_ == "_main_":
    main()
