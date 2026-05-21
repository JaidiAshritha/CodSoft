contacts = {}

def add_contact():
    print("\n========== ADD NEW CONTACT ==========")

    name = input("Enter Name        : ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email       : ")
    address = input("Enter Address     : ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print(f"\n✅ Contact '{name}' added successfully!")

def view_contacts():

    print("\n========== CONTACT LIST ==========")

    if not contacts:
        print("❌ No contacts found.")
        return

    for name, details in contacts.items():
        print(f"""
👤 Name    : {name}
📞 Phone   : {details['Phone']}
📧 Email   : {details['Email']}
🏠 Address : {details['Address']}
----------------------------------------
""")

def search_contact():

    print("\n========== SEARCH CONTACT ==========")

    search = input("Enter Name or Phone Number: ")

    found = False

    for name, details in contacts.items():

        if search.lower() == name.lower() or search == details["Phone"]:

            print(f"""
✅ Contact Found!

👤 Name    : {name}
📞 Phone   : {details['Phone']}
📧 Email   : {details['Email']}
🏠 Address : {details['Address']}
""")
            
            found = True
            break

    if not found:
        print("❌ Contact not found.")

def update_contact():

    print("\n========== UPDATE CONTACT ==========")

    name = input("Enter Contact Name to Update: ")

    if name in contacts:

        print("\nEnter New Details")

        phone = input("New Phone Number: ")
        email = input("New Email       : ")
        address = input("New Address     : ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print(f"\n✅ Contact '{name}' updated successfully!")

    else:
        print("❌ Contact not found.")

def delete_contact():

    print("\n========== DELETE CONTACT ==========")

    name = input("Enter Contact Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print(f"\n🗑 Contact '{name}' deleted successfully!")

    else:
        print("❌ Contact not found.")

while True:

    print("\n" + "=" * 55)
    print("               📒 CONTACT BOOK")
    print("=" * 55)

    print("""
1️⃣  Add Contact
2️⃣  View Contacts
3️⃣  Search Contact
4️⃣  Update Contact
5️⃣  Delete Contact
6️⃣  Exit
""")

    choice = input("Enter Your Choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\n✨ Exiting Contact Book...")
        print("📒 Thank You for Using the Contact Book System!")
        break

    else:
        print("\n❌ Invalid Choice! Please select between 1 and 6.")