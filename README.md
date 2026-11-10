Branch IP Address Validator

Student Details:
Name - Shaun McFadzean
Banner ID - B00410027
Campus - Lanarkshire

Program:

This python program will prompt the user to input an IP address, if the input meets the criteria a valid IP message will be outputted. If the input does not meet the criteria then an invalid IP message will outputted.

Code:

The user will input an IP Address to be validated. The program will take the IP Address, check for dot's if found +1 will be added to the dot_count. If dot_count doesn't = 3 then an invalid IP message will output and the program will end. When only 3 dot's are in the string, the IP address gets split at the dot's, creating a list, with the remaining characters in the IP address splitting into strings. The values in the list will then be checked to see if they are numerical, if not, an invalid IP message will output and the program will end. If the string are only numerical they will be converted into an integer. Once converted the number will be checked to see if its within the 0-255 range, if it is +1 will be added to num_count. If num_count = 4 and dot_count = 3 a True value is returned a valid Ip message will output and the program will ends. If num_count != 4 and/or dot_count != 3 an invalid IP messgae will output.

How To Run:
1. Run program
2. Input IP address, message will output depending on input, program ends.
