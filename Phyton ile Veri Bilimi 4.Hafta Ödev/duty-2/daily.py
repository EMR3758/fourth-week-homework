import os
    

def dailyNoteAdd():
    with open("/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/duty-2/daily.txt","a") as daily:
        while True:
            a = input("Write down the things you want to add to your diary.(Type 'exit' to exit.):  ")
            
            if a.lower() == "exit":
                break
            daily.write(f"\n********\n{a}\n********")
    print("The student has been added successfully")


def dailyNoteShow():
    with open("/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/duty-2/daily.txt","r") as daily:
        print(daily.read())
        


def dailyNoteRemove():
    b = input("Do you want to delete the file? (Press 'y' for yes): ")
    if b.lower() == "y":
        if os.path.exists("/Users/emirhanozcan/Documents/GitHub/fourth-week-homework/duty-2/daily.txt"):
            os.remove("/Users/emirhanozcan/Documents/GitHub/fourth-week-homework/duty-2/daily.txt")
            print("The file has been removed.") 
        else:
            print("daily.txt file not found")
    
def Menu():
    while True:
        print("\nMENU")
        print("1-Note add for daily.")
        print("2-Show daily notes. ")
        print("3-Remove file.")
        print("4-Exit")
        vote = input("Make a choice: ")
        
        if vote == "1":
            dailyNoteAdd()
        elif vote == "2":
            dailyNoteShow()
        elif vote == "3":
            dailyNoteRemove()
        elif vote == "4":
            print("The program is exiting.")
            break
        else:
            print("Invalid selection, please select again.")



Menu()
        