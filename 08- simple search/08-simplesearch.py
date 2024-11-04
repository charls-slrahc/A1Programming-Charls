names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

user_input = input("Enter the name your looking for: ")

# Search for the term in the list
if user_input in names:
    print(f"{user_input} is found in the list.")
else:
    print(f"{user_input} is not found in the list.")
