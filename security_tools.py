#Securtiy tools
import random
def val_pass(passwd):
    passwd = passwd.strip()
    alp = 0 #counts for character input
    num = 0
    sym = 0
    if len(passwd) >= 10: #True or False output depeding on password length
        length = True
    else:
        length = False

    for char in passwd: #checking characters and adding to correct count
        if char.isalpha():
            alp += 1
        elif char.isnumeric():
            num += 1
        else:
            sym +=1
    
    if length == True and alp >= 1 and num >= 1 and sym >= 1:
        print("Password accepted") #Prints if criteria is met
    else:
        print("Password not accepted") #Prints if criteria is not met
        print(rand_pass()) #Calls function to create a strong enough password to suggest to the user

def val_ip(ip):
    dot = 0 #counts for character inputs
    num = 0
    any = 0
    for char in ip: #checks to see if input contains "."
        if char == ".": #Adds 1 to count for every "." 
            dot += 1
    ip_split = ip.split(".") #split using "." as a delimetor 
    ip_len = len(ip_split) #checks length of ip_split
    if ip_len == 4:                       
        for index in range(4): #Reiterates through every index in list
            pop = ip_split.pop() #Pop out value
            if pop.isnumeric():#Checks to see if popped value is numeric
                pop = int(pop) #Converts numeric value to an int
                if pop >= 0 and pop <= 255: #Adds 1 to count if pop is inbetween 0 and 250
                    num += 1
            else:
                any += 1 #Adds 1 to count if popped value isnt numeric

    if num == 4 and dot == 3 and any == 0:
        print("IP is valid") #only prints if if statement is correct
    else:
        print("IP is not valid") #only prints if incorrect

def rand_pass():
    characters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!£$%&?" #string with every avaliable character that can be used to create a password
    length = random.randint(10, 16) #Creates random password length
    passwd = "" #Empty string for password
    for char in range(length): #Reiterates adding a random character from "characters" into "passwd" depedning on "length" value
        passwd += random.choice(characters) #Adding character to passwd
    print(f"Password is not strong enough.\nHere is a randomly generated strong passsowrd: {passwd}") #Prints once for loop is finished