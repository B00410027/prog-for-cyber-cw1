#IP Address Validator (Using Function)

def validate_ip(input):
    print("---"*15)
    input = input
    dot_count = 0 #count to check .
    num_count = 0 #count to check numbers
    replace_input = input.replace(" ", "") #remove whitespace

    for char in replace_input:
        if char == ".": #Adds 1 to count if . is found
            dot_count += 1
    if dot_count == 3: #remoevs . if 3 is found
        split_input = replace_input.split(".")
        for num in split_input: #Iterates through every index
            try:
                num = int(num) #Coverts string from list into an int
            except ValueError:
                break
            if num >=0 and num <=255: 
                num_count += 1 #Adds 1 to count if num is in range 0-255
    if num_count == 4 and dot_count == 3:   
            print(replace_input) #Prints if num_count == 4 and dot_count == 3
            return True

input = input("ENTER IP ADDRESS: ") #user input
boolean = validate_ip(input)
if boolean == True:
    print("IP Address is valid.")#Prints if IP is valid
else:
    print(input)
    print("IP Address is not valid.")#Prints if IP address isnt valid
