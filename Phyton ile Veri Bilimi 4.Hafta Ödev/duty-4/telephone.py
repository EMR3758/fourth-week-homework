import os

file_path = "/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/duty-4/telephone.txt"

def addTelephone():
    with open(file_path, "a", encoding="utf-8") as tel:
        while True:
            user_name = input("Enter your name: ")
            user_surname = input("Enter your surname: ")
            user_tel_number = input("Enter your tel number: ")

            tel.write(f"{user_name} {user_surname},{user_tel_number}\n")
            print("The telephone number has been added successfully.")

            exit_command = input("Type 'exit' to exit or press 'n' to continue: ")
            if exit_command.lower() == "exit":
                break

def searchTelephone():
    search_name = input("Which person's number? ")
    try:
        with open(file_path, "r", encoding="utf-8") as tel:
            found = False
            for row in tel:
                person, telephone = row.strip().split(",")
                if person.lower() == search_name.lower():
                    print(f"{person} person's telephone number: {telephone}")
                    found = True
                    break
            
            if not found:
                print("Person not found")
    except FileNotFoundError:
        print("Guide not found. You must add people first.")

def listTelephone():
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r", encoding="utf-8") as tel:
            print("\n--- Telephone Directory ---")
            print(tel.read())
    else:
        print("Telephone directory is empty.")

def menu():
    while True:
        print("\nMENU")
        print("1 - Add a telephone number")
        print("2 - Search for a telephone number")
        print("3 - List all telephone numbers")
        print("4 - Exit")

        choice = input("Make a choice: ")

        if choice == "1":
            addTelephone()
        elif choice == "2":
            searchTelephone()
        elif choice == "3":
            listTelephone()
        elif choice == "4":
            print("The program is exiting.")
            break
        else:
            print("Invalid selection, please try again.")

menu()
