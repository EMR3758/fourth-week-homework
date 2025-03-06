import json
import os

def userAdd():
    file_path = "/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/duty-3"
    users = []

    
    while True:
        user_name = input("Enter your name: ")
        user_surname = input("Enter your surname: ")
        user_age = input("Enter your age: ")

        user_data = {
            "name": user_name,
            "surname": user_surname,
            "age": user_age
        }

        users.append(user_data) 

        exit_command = input("Type 'exit' to exit or press 'n' to continue: ")
        if exit_command.lower() == "exit":
            break

    
    with open(file_path, "w", encoding="UTF-8") as user_file:
        json.dump(users, user_file, indent=4, ensure_ascii=False)

    print("Users saved successfully!")

def showUser():
    file_path = "/Users/emirhanozcan/Documents/GitHub/fourth-week-homework/duty-3/user.json"
    with open(file_path,"r",encoding="UTF-8") as user_file:
        data = json.load(user_file)
        print(data)

def Menu():
    while True:
        print("--------------\n Menu    \n--------------")
        print("1-User Add.")
        print("2-Show users.")
        print("3-Exit\n--------------")
        choice = input("Make a choice: ")
        if choice == "1":
            userAdd()
        elif choice == "2":
            showUser()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid input.Log in again.")


Menu()
