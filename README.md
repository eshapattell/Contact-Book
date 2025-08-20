# 📒 Contact Book

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) 
[![Status](https://img.shields.io/badge/status-active-success.svg)]()  

---

# 📌 Project Overview
The *Contact Book* is a Python-based application designed to manage your personal or professional contacts efficiently.  
It simulates a real-world phonebook, but with the added benefit of being implemented using *data structures* for learning purposes.  

Unlike a simple dictionary-based contact manager, this project uses a *self-referential linked list, where each contact node stores the person’s **name, phone number, and email address, along with a pointer to the next contact. This ensures that the contacts remain **sorted alphabetically* as new entries are added, making searching and navigation intuitive.  

Additionally, the project implements *file persistence*: contacts are automatically saved to a file when the program exits and reloaded when it starts. This provides a continuous experience where your data is never lost, even if the program is restarted.  

This project demonstrates concepts from *Data Structures and Algorithms (DSA)* such as linked lists, insertion in sorted order, traversal, and deletion, combined with *file handling* in Python. It is an excellent learning project for students, beginners in Python, or anyone who wants to understand how data structures can be applied to solve real-world problems.  

In short:  
- 📒 Acts as a lightweight and easy-to-use *digital contact book*  
- 🧠 Reinforces *linked list fundamentals*  
- 💾 Demonstrates *persistent storage* with Python file I/O  
- 🚀 A great stepping stone for bigger projects like CRM systems or contact management apps with GUIs
---

# ✨ Features

✔ *Add New Contacts*  
Easily add new contacts by providing a name, phone number, and email. The system automatically places the new contact in *alphabetical order* in the linked list for organized storage.  

✔ *Search Contacts*  
Quickly look up a contact by name. The program traverses the linked list to locate the entry and displays the contact’s details instantly.  

✔ *Update Contact Information*  
Modify an existing contact’s phone number or email without having to delete and re-add them. This ensures your contact book always stays current.  

✔ *Delete Contacts*  
Remove contacts seamlessly by name. The linked list updates itself dynamically to close gaps and keep data consistent.  

✔ *Show All Contacts*  
Display all saved contacts in a neat, alphabetically sorted list. Perfect for browsing when you don’t remember the exact spelling of a name.  

✔ *Persistent File Storage*  
All contacts are saved to a file (contacts.pkl) using Python’s *pickle module*. Even if you close the program, your data is automatically reloaded the next time you open the contact book.  

✔ *Lightweight & Dependency-Free*  
Built using only Python’s standard library. No external dependencies are required — making it easy to run on any machine with Python 3.9+.  

✔ *User-Friendly Console Menu*  
Interactive, menu-driven interface that makes it easy to navigate options, even for beginners.

---

# 🧠 Data Structures
### **Linked List**
- Each node stores: Name, Phone Number, Email, Next pointer  
- Sorted alphabetically by name during insertion  

### **File Storage**
- Contacts saved in `contacts.txt`  
- Loaded at program start  
- Updated automatically after changes  

---

# 🧮 Working Logic
1️⃣ **Add Contact** → Insert node into linked list in alphabetical order  
2️⃣ **Search Contact** → Traverse list to find match  
3️⃣ **Update Contact** → Find node & modify values  
4️⃣ **Delete Contact** → Remove node from list & update file  
5️⃣ **File Sync** → Save changes to file automatically  

---

# 📦 Project Layout


contact\_book/
├── app.py          # Demo application
├── contactbook.py  # Core classes and logic
└── README.md       # Documentation

`

---

# 🚀 Quick Start
Run the demo locally:

bash
python3 app.py
`

This will:         
👉 Load contacts from file (if any)           
👉 Allow adding, searching, updating, deleting contacts          
👉 Save all changes automatically          

---

# 🧪 Example Output


📒 Contact Book
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Show All Contacts
6. Exit

Choose an option: 1
Enter Name: Alice
Enter Phone: 9876543210
Enter Email: alice@mail.com
✅ Contact added successfully!

Choose an option: 5
Contacts:
- Alice | 9876543210 | alice@mail.com


---

# 🖼️ Screenshot (Sample Run)


-------------------------------------
📒 CONTACT BOOK - PYTHON SIMULATOR
-------------------------------------

1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Show All Contacts
6. Exit

👉 User adds "Bob":
✅ Contact added successfully!

👉 User lists all contacts:
Contacts:
- Alice | 9876543210 | alice@mail.com
- Bob   | 9123456780 | bob@mail.com


---

# 🧩 Extending the Project           

🔹 Export contacts to CSV or JSON         
🔹 Add GUI with Tkinter or PyQt         
🔹 Multi-field search (by number/email)           
🔹 Grouping contacts by tags (Family, Work, Friends)         
🔹 Cloud sync option         

---

# ⚙️ Requirements

* **Python 3.9+**
* Uses only standard library modules: `dataclasses`, `os`, `pickle` (or `json`)

---

# 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
✔ Free to use, modify, and distribute with attribution.
✔ No liability for issues arising from use.

---

# 📊 Status

🟢 **Active** → This project is being maintained and improved.
