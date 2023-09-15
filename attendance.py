students = {}

while True:
    print("\n============================================\n")
    MODE = int(input("What would you liek to perform?\n\n[1] Register Student\n[2] Mark Attendance\n[3] Check Attendance\n[4] Exit\n\nYour Input: "))
    if MODE == 1:
        rollnumber = int(input("Enter the roll number of the student: "))
        if students.get(rollnumber) != None:
            print(f"This roll number already belongs to student: {students[rollnumber]['name']}")
            input("\nPress enter to continue...")
        else:
            name = input("Enter the name of the student: ")
            students[rollnumber] = {"name": name, "attendance": 0}
            print(f"[{rollnumber}] {name} has been successfully registered!")
            input("\nPress enter to continue...")
        
    elif MODE == 2:
        rollnumber = int(input("Enter your roll number: "))
        if students.get(rollnumber) == None:
            print("You have not registered as a student yet!")
            input("\nPress enter to continue...")
        else:
            students[rollnumber]['attendance'] += 1
            print(f"Welcome back, {students[rollnumber]['name']}! You have successfully marked your attendance for today.")
            input("\nPress enter to continue...")
    
    elif MODE == 3:
        rollnumber = int(input("Enter the roll number of the student: "))
        if students.get(rollnumber) == None:
            print("The student with the provided roll number does not exists.")
            input("\nPress enter to continue...")
        else: 
            print(f"Attendance of student {students[rollnumber]['name']}: {students[rollnumber]['attendance']}")
            input("\nPress enter to continue...")
    elif MODE == 4:
        exit()