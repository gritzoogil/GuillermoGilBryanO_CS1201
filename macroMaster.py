user_accounts = {}

def tdee(height, weight, sex, age, activity):
    if sex == "m":
        return round(((4.799 * float(height) + 13.397 * float(weight) - (5.677 * age)) + 88.362) * activity) # tdee for male
    else:
        return round(((3.098 * float(height) + 9.247 * float(weight) - (4.330 * age)) + 447.593) * activity) # tdee for female
    
def goal(calculated_tdee, weight, username):
    # Cut or Bulk
    print("\n1. Cut")
    print("2. Bulk")
    while True:
        choice = input("")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 2:
                if choice == 1:
                    user_accounts[username]['goal'] = "cut" # set goal to cut
                    calories, p, f, c = cut_cal(calculated_tdee, weight)
                elif choice == 2:
                    user_accounts[username]['goal'] = "bulk" # set goal to bulk
                    calories, p, f, c = bulk_cal(calculated_tdee, weight)
                
                # assign values to user's account
                user_accounts[username]['calories'] = calories
                user_accounts[username]['protein'] = p
                user_accounts[username]['fat'] = f
                user_accounts[username]['carb'] = c
                print("\n")
                main()  # back to main menu
                break
            else:
                print("Please enter a number between 1 and 2.")
        else:
            print("Please enter a number between 1 and 2.")

def cut_cal(tdee, weight):
    # cut calories
    while True:
        loss_per_week = float(input(f"\n% loss per week (between 0.5 and 1): "))
        if 0.5 <= loss_per_week <= 1:
            break
        else:
            print("\nPlease enter a percentage between 0.5 and 1.")

    loss_per_week /= 100
    w = float(weight) * 2.20462 # converts weight into pounds (lb)
    calories = round(tdee - loss_per_week * w * 500)
    p = round(float(w) * 0.82) # 0.82g of protein per lb of bodyweight
    f = round(float(w) * 0.3) # 0.3g of fat per lb of bodyweight
    c = round((calories - (p * 4 + f * 9)) / 4) # rest of the calories are carbs
    return calories, p, f, c

def bulk_cal(tdee, weight):
    # bulk calories
    while True:
        gain_per_week = float(input(f"\n% gain per week (between 0.25 and 0.5): "))
        if 0.25 <= gain_per_week < 0.5:
            break
        else:
            print("\nPlease enter a percentage between 0.25 and 0.5.")

    gain_per_week /= 100
    w = float(weight) * 2.20462 # converts weight into pounds (lb)
    calories = round(tdee + gain_per_week * w * 500)
    p = round(float(w) * 0.82) # 0.82g of protein per lb of bodyweight
    f = round(float(w) * 0.3) # 0.3g of fat per lb of bodyweight
    c = round((calories - (p * 4 + f * 9)) / 4) # rest of the calories are carbs
    return calories, p, f, c

def register():
    print("\n")
    while True: # create account 
        username = input("Enter a username (Leave blank to go back): ")
        if username in user_accounts:
            print("Username already taken.")
        elif username.strip() == "":
            print("\n")
            main()
            break
        else:
            while True:
                password = input("Enter a password: ")
                user_accounts[username] = {'password': password}
                break
        break
    
    while True: # input sex
        sex = input("Sex (m/f): ")
        if sex.lower() in ['m', 'f']:
            break
        else:
            print("\nEnter 'm' for male or 'f' for female. ")

    print("\nUnit for weight:")
    print("1. KG")
    print("2. LB")
    while True:
        choice = input("")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 2:
                if choice == 1:
                    to_kg = 1
                elif choice == 2:
                    to_kg = 0.45359237
                break
            else:
                print("\nEnter a number between 1 and 2.")
        else:
            print("\nEnter a number between 1 and 2.")
    
    while True: # input weight
        weight =  input("\nWeight: ")
        try:
            weight = round(float(weight) * to_kg, 2)
            if 30 <= weight <= 250: 
                break
            else:
                print("\nPlease enter a valid weight.")
        except ValueError:
            print("\nPlease enter a valid weight.")
    
    print("\nUnit for height: ")
    print("1. CM")
    print("2. IN")
    while True:
        choice = input("")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 2:
                if choice == 1:
                    to_cm = 1
                elif choice == 2:
                    to_cm = 2.54
                break
            else:
                print("\nEnter a number between 1 and 2.")
        else:
            print("\nEnter a number between 1 and 2.")
    
    while True: # input height
        height = input("\nHeight: ")
        try:
            height = round(float(height) * to_cm, 2)
            if 100 <= height <= 200:
                break
            else:
                print("\nPlease enter a valid height.")
        except ValueError:
            print("\nPlease enter a valid height.")
    
    while True: # input age
        age = input("\nAge: ")
        if age.isdigit():
            age = int(age)
            if 10 <= age <= 100:
                break
            else:
                print("\nPlease enter a valid age.")
        else:
            print("\nPlease enter a valid age.")
        
    print("\nActivity level: ") # multiplier to bmr to compute tdee
    print("1. Sedentary (minimal to no exercise)")
    print("2. Lightly Active (exercise lightly 1-3 days a week)")
    print("3. Moderately Active (exercise moderately 3-5 days a week)")
    print("4. Very Active (hard exercise 6-7 days a week)")
    print("5. Extra Active (very hard exercise 6-7 days a week or have a physical job)")
    while True: # input activity level
        choice = input("")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                if choice == 1:
                    activity = 1.2
                elif choice == 2:
                    activity = 1.375
                elif choice == 3:
                    activity = 1.55
                elif choice == 4:
                    activity = 1.725
                elif choice == 5:
                    activity = 1.9
                break
            else:
                print("\nEnter a number between 1 and 5.")
        else:
            print("\nEnter a number between 1 and 5.")
    
    calculated_tdee = tdee(height, weight, sex, age, activity)
    goal(calculated_tdee, weight, username)

def logged_in_menu(username): # display logged in menu
    # access user info from user_accounts
    user_info = user_accounts[username]
    print(f"\nLogged in as {username}")
    # display goal, calories, and macros
    print(f"Goal: {user_info['goal']}")
    print(f"Calories: {user_info['calories']}cal")
    print(f"Protein: {user_info['protein']}g")
    print(f"Fat: {user_info['fat']}g")
    print(f"Carb: {user_info['carb']}g")
    print("\n1. Log out")
    while True:
        choice = input("")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("\n")
                main() # back to main menu
                break
            else:
                print("Enter 1 to log out.")
        else:
            print("Enter 1 to log out.")

def main(): # display welcome menu
    print('*'*23)
    print("Welcome to Macro Master")
    print('*'*23)
    print("1. Register User")
    print("2. Login")
    print("3. Exit")
    while True:
        choice = input("")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                if choice == 1:
                    register()
                elif choice == 2:
                    while True:
                        username = input("\nUsername (leave blank to go back.): ")
                        if username in user_accounts:
                            while True:
                                password = input("Password: ")
                                if password == user_accounts[username]['password']:
                                    logged_in_menu(username)
                                    break
                                else:
                                    print("Wrong password. Try again.")
                            break
                        elif username.strip() == "":
                            print("\n")
                            main() # back to main menu
                            break
                        else:
                            print("User not found. Try again.")
                elif choice == 3:
                    raise SystemExit # exit
                break
            else:
                print("Please enter a number between 1 and 5.")
        else:
            print("Please enter a number between 1 and 5.")



if __name__ == '__main__':
    main()
