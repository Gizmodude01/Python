import os
from datetime import datetime

user = os.environ.get('USERNAME', 'default_user')
debug_log_path = os.path.join("C:","Users",user,"Videos","Code Trash", "DebugLog")
if not os.path.exists(debug_log_path):
    os.makedirs(debug_log_path)


def debug_numberAdditionLog(*args):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        with open(os.path.join(debug_log_path, "numberAdditionLog.txt"), "a") as output:
            output.write(timestamp + " " + " ".join(map(str, args)) + "\n")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")

debug_numberAdditionLog("Debug log for Number Addition capability.\n")

numbers = []


def numInput():
    while True:
        num = input("Please enter a number (or 'done' to finish): ")
        debug_numberAdditionLog("entered:", num )

        if num.lower() == 'done':
            debug_numberAdditionLog("Breaking loop...")
            break
        try: 
            numbers.append(int(num))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            debug_numberAdditionLog("Invalid number has been entered")

    numSummation()

    print("Numbers entered:", numbers)
    debug_numberAdditionLog("Numbers entered:", numbers)


def numSummation():

    total = 0

    for number in numbers:
        total += number
        
    print("The sum is:", total)
    debug_numberAdditionLog("Array Sum:", total)

    numbers.clear()
    numInput()

numInput()





