import os
os.system('cls')


print("STUDENT INFORMATION SYSTEM")
print("-----------------------------------\n")

student_records = {}

while True:
    print("SELECT FROM THE OPTION BELOW \nA- Add Information\nB- Print All\nC- Search\nD- Delete a Record\nE- Modify a Record\nF- Exit")
    
    choice = input("Your choice  --->").lower()
    
    if choice == 'a':
        os.system('cls')
        print("ADDING STUDENT INFORMATION")
        print("-----------------------")
        search_code = input("Key search for this student  ").upper()
        first_name = input("Input student first name  ").upper()
        last_name = input("Input student last name  ").upper()
        course = input("Input student course  ").upper()
        email = input("Input student email adress  ").upper()
        isSingle = input("Are you single (true or false) --> ")
        
        student_record = {search_code : [first_name, last_name, course, email, isSingle] }
        print("DATA SAVED")

        os.system('cls')
        continue

    elif choice == 'b':
        os.system('cls')
        print("PRINT STUDENT RECORD")

        for id, record in student_record.items():
            print(f"STUDENT ID {id} in STUDENT RECORD {record}")
        continue

    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        print("=========================== ")

        search_id = input("input ID to search ---> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("================")
                print("\n\nRECORD FOUND")
                print("================")
                #print the record of search student
                for i in student_records[search_id]:
                    print(f"-- {i}")        
            else:
                print("================")
                print("\n\nNO RECORD FOUND")
                print("================")
        continue    

    elif choice == 'd':
        os.system('cls')
        print("DELETE EXISTING RECORD")

        search_id = input("input ID to search ---> ").lower()

    
        if search_id in student_records.keys():
            print("================")
            print("\n\nRECORD FOUND")
            print("================")
                #print the record of search student
            for i in student_records[search_id]:
                print(f"-- {i}")  

            student_records.pop(search_id)
            print("RECORD DELETED")

        else:
            print("================")
            print("\n\nNO RECORD FOUND")
            print("================")

        continue

    elif choice == 'e':
        print("EDITING/MODIFY RECORD")

        search_id = input("input ID to search ---> ").lower()

    
        if search_id in student_records.keys():
            print("================")
            print("\n\nRECORD FOUND")
            print("================")
                #print the record of search student
            for i in student_records[search_id]:
                print(f"-- {i}")  

                search_code = input("Key search for this student  ").upper()
                first_name = input("Input student first name  ").upper()
                last_name = input("Input student last name  ").upper()
                course = input("Input student course  ").upper()
                email = input("Input student email adress  ").upper()
                isSingle = input("Are you single (true or false) --> ")

                student_records[[search_id][0]] = first_name
                student_records[[search_id][1]] = last_name
                student_records[[search_id][2]] = course
                student_records[[search_id][3]] = email
                student_records[[search_id][4]] = isSingle

                
                student_record = {search_code : [first_name, last_name, course, email, isSingle] }
                print("DATA UPDATED")
            

                continue

        
    elif choice == 'f':
        print("System Exit")
        break
    else:
        print("invalid choice")