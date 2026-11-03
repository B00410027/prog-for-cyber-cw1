
print("Welcome to the security tool")
print("----"*45)

#input for menu choice
input1 = input("Press 1 for Security Event Counter \nPress 2 for Brute Force Simulation \nPress 3 for Login Authentication \nPress 4 to Exit \n>> ")
#constant value for security event counter
SEC_password = "password"

if input1 == "1": 
    print("Security Event Counter")
    print("----"* 45)
    #constant password
    sec_password = "password"
    #counts for user guesses
    correct_count = 0
    incorrect_count = 0
    count = 1
    while count <= 10: #Reiterates through loop until count == 10
        guess = input("Enter password >> ") #Prompt user input
        count = count + 1 #Adds 1 to count every reiteration 
        if guess == sec_password: #adds to correct_count if guess == "password"
            correct_count = correct_count + 1
        else: #adds to incorrect_count if guess != "password"
            incorrect_count = incorrect_count + 1
    #takes the incorrect_count and converts it into a percentage
    percentage = (incorrect_count / 10) * 100
    if percentage > 50: #Prints if percentage is > 50
        print("Security Alert!", percentage,"% of password attemots where incorrect.")
    else: #Prints if percentage is <= 50
        print(percentage,"% of your password attempts where incorrect.")

elif input1 == "2":
    print("Brute Force Simulation")
    print("----"*45)
    bf_password = "bruteforce"
    #counts for users guesses
    count = 0
    guess_count = 0
    print("You have 5 guesses at the correct password") #Tells user the maximum amount of attempts
    while count < 5: #Reiterates through loop until count is => 5 or "bruteforce" has been guessed
        guess = input("Enter password >> ") #Prompt user input
        count = count + 1 #Adds 1 to count every reiteration
        if guess == bf_password:  #Prints and breaks loop if guess == "bruteforce"
            print("Password accepted")
            break
        elif count == 5: #Prints when maximum amount of attempts have been used
            print("Maximum attempts used")
        else: #Prints when guess != "bruteforce"
            print("Incorrect try again")


elif input1 == "3":
    print("Authentication")
    print("----"*45)
    #count for user guesses
    guess = 1
    while guess <= 3: #Reiterates through loop until guess == 4 (user has 3 guesses)
        username = input("Enter username >> ")
        password = input("Enter password >> ")
        guess = guess + 1
        if username == "username" and password == "password":
            print("Authentication successful") #Prints and breaks if BOTH user inputs match "username" and "password"
            break
        else:
            print("Authentication failed") #Prints if either of the user gueeses != "username" and/or "password"
            if guess == 4:
               print("Due to max attempts reached this account has been frozen for 24 hours") #Prints when user guesses == 4 (3 Guesses total)

elif input1 == "4": #Prints when user wants to leave program
    print("Thank you for using the Security Tool")

else: #Prints if user input1 != "1", "2", "3" or "4"
    print("Input not recognised, please try again")
