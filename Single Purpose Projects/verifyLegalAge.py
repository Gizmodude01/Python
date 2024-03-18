try:
    if (age := int(input("Please enter your age: "))) >= 18 and age < 120:
        print(f"User is {age} and is allowed to vote")
    elif age > 120 or age <= 3:
        print(f"{age} is not valid, please enter a real age")
    else: 
         print(f"User is {age} and is NOT allowed to vote")
except ValueError:
    print(f"Value is an invalid input")
