def even_or_odd(number):

    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
   
    user_input = input("Please enter a number: ")
    
   
    try:
        number = int(user_input)
        
        result = even_or_odd(number)
        
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()