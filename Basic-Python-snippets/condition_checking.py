import sys
while True:
    name = input("Enter your name: ")
    if name.lower() == "gangadhar":
        print("Hello Gangadhar")
        i=3
        while(i>0):
            password = input("Enter your password: ")
            if password.lower()== "fish":
                print("You are logged in")
                sys.exit()
            else:
                print("Invalid password. Try again.")  
            i-=1
        print("You have entered wrong password 3 times. Exiting...")
    else:
        print("Invalid name")
        sys.exit()
        
        
