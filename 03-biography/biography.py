#user input

name = input("Please enter your name (First and last): ")
hometown = input("Please enter your howntown: ")

#valid number only

while True:
        age_input = input("Enter your age: ")
        try:
            age = int(age_input)  # Attempt to convert age to an integer
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input for age. Please enter a numeric value.")
      
#user information dictionary

user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(f"hello my name is {user_info['name']}")
print(f"i am from {user_info['hometown']}")
print(f"i am {user_info['age']} years old")