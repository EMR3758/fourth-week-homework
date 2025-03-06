def studentsAdd():
    with open("/Users/emirhanozcan/Desktop/veri bilimi ödev/Phyton ile Veri Bilimi 4.Hafta Ödev/duty-1/ogrenciler.txt","a") as ogrenci:
        while True:
            student = input("Enter student name (Type 'done' to exit.): ")
            if student.lower() == "done":
                break
            ogrenci.write(student + "\n")
    print("The student has been added successfully.")
            
studentsAdd()