import random

object = {}

while True:
    MODE = int(input("What would you like to do?\n[1] Login\n[2] Register\n[3] Exit:\nEnter your reply: "))
    if MODE == 1:
        username = input("Enter the username: ")
        if object.get(username) == None:
            print("User not found")
            input("\n\nPress enter to continue...")
        if object.get(username) != None: 
            password = input("What is your pasword: ")
            if object.get(username) != password:
                fp = int(input("Incorrect Password! Did you forget your password?\n[1] Re-Login\n[2] Forgot Password\n\nEnter Your reply: "))
                if fp == 1:
                    continue
                elif fp == 2:
                    otp = random.randint(1000, 9999)
                    otpreply = int(input(f"An OTP has been sent to your device! Please enter the OTP [{otp}]: "))
                    if otp == otpreply:
                        password = input("Enter the new Password: ")
                        object[username] = password
                        print("Password has been updated!")
                        input("\n\nPress enter to continue...")
                    else:
                        print("Incorrect OTP! Please try logging in again!")
                        input("\n\nPress enter to continue...")
            else:
                print("User Authorized!")
                input("\n\nPress enter to continue...")
        
    else:
        if MODE == 2:
            username = input("Enter youtr username: ")
            password = input("Enter your password: ")
            object[username] = password
            print("You have successfully regustered.")
            input("\n\nPress enter to continue...")

        if MODE == 3:
            exit()