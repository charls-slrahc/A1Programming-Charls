#define the correct password 

correct_password =  "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    enter_password = input("Please enter your password: ")  

    if enter_password == correct_password:
        print("Access Granted")
        break #to end the loop
    else:
        attempts += 1 
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Access denied, you have {remaming_attempts} attempts remaining.")
        else:
            print("inncorrect password. Maximum attempts reached. Please try again later. ")
        
