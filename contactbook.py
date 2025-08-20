import os
import pickle
from dataclasses import dataclass
from typing import Optional


@dataclass
class Contact:
    name: str
    phone: str
    email: str
    next: Optional["Contact"] = None  # linked list pointer


class ContactBook:
    def _init_(self, filename="contacts.pkl"):
        self.head: Optional[Contact] = None
        self.filename = filename
        self.load_contacts()

    # Insert alphabetically
    def add_contact(self, name: str, phone: str, email: str):
        new_contact = Contact(name, phone, email)

        # Insert at head if list is empty or should be first alphabetically
        if self.head is None or name.lower() < self.head.name.lower():
            new_contact.next = self.head
            self.head = new_contact
        else:
            curr = self.head
            while curr.next and curr.next.name.lower() < name.lower():
                curr = curr.next
            new_contact.next = curr.next
            curr.next = new_contact

        self.save_contacts()
        print(f"✅ Contact '{name}' added successfully!")

    # Search by name
    def search_contact(self, name: str) -> Optional[Contact]:
        curr = self.head
        while curr:
            if curr.name.lower() == name.lower():
                return curr
            curr = curr.next
        return None

    # Update existing contact
    def update_contact(self, name: str, new_phone: str, new_email: str):
        contact = self.search_contact(name)
        if contact:
            contact.phone = new_phone
            contact.email = new_email
            self.save_contacts()
            print(f"✏️ Contact '{name}' updated successfully!")
        else:
            print(f"⚠️ Contact '{name}' not found.")

    # Delete a contact
    def delete_contact(self, name: str):
        curr = self.head
        prev = None
        while curr:
            if curr.name.lower() == name.lower():
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                self.save_contacts()
                print(f"🗑️ Contact '{name}' deleted successfully!")
                return
            prev, curr = curr, curr.next
        print(f"⚠️ Contact '{name}' not found.")

    # Show all contacts
    def show_all_contacts(self):
        if self.head is None:
            print("📭 No contacts available.")
            return
        print("\n📒 Contacts List:")
        curr = self.head
        while curr:
            print(f"- {curr.name} | {curr.phone} | {curr.email}")
            curr = curr.next

    # File persistence methods
    def save_contacts(self):
        contacts = []
        curr = self.head
        while curr:
            contacts.append((curr.name, curr.phone, curr.email))
            curr = curr.next
        with open(self.filename, "wb") as f:
            pickle.dump(contacts, f)

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "rb") as f:
            try:
                contacts = pickle.load(f)
                for name, phone, email in sorted(contacts, key=lambda x: x[0].lower()):
                    self.add_contact(name, phone, email)
            except EOFError:
                pass
