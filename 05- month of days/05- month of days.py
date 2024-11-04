month_days = {
    1: 31,  # January
    2: 28,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31  # December
}

# nigger
month = int(input("Please enter the month number: "))

if month == 2:
    leapyear = input("is your year a lleap year?, yes or no: ")
    while True:
        if leapyear == "yes":
            month_days[2] = 28
            break
        elif leapyear == "no":
            month_days[2] = 29
            break
        else:
            leapyear = input("Invalid input. Please enter only 'yes' or 'no': ")

# nigger
if month < 1 or month > 12:
    print("Invalid month number, please enter a motnh number: ")

else:
    print(f"The month {month} has {month_days[month]} days.")