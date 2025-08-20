from contactbook import ContactBook

def main():
    book = ContactBook()

    while True:
        print("\n-------------------------------------")
        print("📒 CONTACT BOOK")
        print("-------------------------------------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter Name to Search: ")
            contact = book.search_contact(name)
            if contact:
                print(f"🔍 Found: {contact.name} | {contact.phone} | {contact.email}")
            else:
                print("⚠️ Contact not found.")

        elif choice == "3":
            name = input("Enter Name to Update: ")
            new_phone = input("Enter New Phone: ")
            new_email = input("Enter New Email: ")
            book.update_contact(name, new_phone, new_email)

        elif choice == "4":
            name = input("Enter Name to Delete: ")
            book.delete_contact(name)

        elif choice == "5":
            book.show_all_contacts()

        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
