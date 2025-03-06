import time
import threading
from datetime import datetime

file_path = "/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/duty-5/log.py"

def log():
    while True:
        with open(file_path, "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"System is running at {timestamp}\n")
        time.sleep(10)

def showLog():
    try:
        with open(file_path, "r", encoding="utf-8") as log_file:
            logs = log_file.readlines()
            print("\nSystem Logs:")
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("Log file not found.")

def menu():
    logging_thread = None  # Log işlemi için thread saklamak için değişken
    
    while True:
        print("\nMENU")
        print("1 - Start logging system activity")
        print("2 - View logs")
        print("3 - Exit")
        choice = input("Make a choice: ")

        if choice == "1":
            if logging_thread is None or not logging_thread.is_alive():
                logging_thread = threading.Thread(target=log, daemon=True)
                logging_thread.start()
                print("Logging has started...")
            else:
                print("Logging is already running.")
        elif choice == "2":
            showLog()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")

menu()
