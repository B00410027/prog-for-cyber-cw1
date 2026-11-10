Branch Cyber Security Utilities 

Student Details: 
Name - Shaun McFadzean 
Banner ID - B00410027 
Campus - Lanarkshire

Program:

This python program will prompt the user to input an IP address and a password. If the IP address meets the criteria a valid IP message will be outputted. If the IP address does not meet the criteria an invalid IP message will be outputted. If the password meets the criteria a password accepted message will be outputted. If the password does not meet the criteria an invalid password message will be outputted along with a random password between 10-16 characters long.

Code:

The user will input an IP Address and a password. The IP will be checked for dots and if one if found +1 is added to dot. Then the IP address will be split at the dots, creating a list, if the list has 4 index, the program will then pop each out value and check to see if it is numerical. If the value is numerical, the string is then converted into an integer and then checked to see if it is within the 0-255 range, if the integer is +1 will be added to num. If the string isn't numerical then +1 is added to any. If num = 4 and dot = 3 and any = 0, a valid IP message will print. If not then an invalid IP message will print. The password will be checked to see if the length is >= 10, a true or false value will ne returned depending on the length. Then each character in the password is checked and adding to the corresponding count, numerical character = +1 to num, alphabetical character +1 to alp and anything else +1 to sym. If length = true and alp, num and sym are all >= 1, then a password accepted message will output, if not a password not accepted message will output, followed by a random password suggested to the user. The rand_pass function will take a random length between 10-16 and will take a matching amount of random characters from the string called characters. It will add these characters to passwd, which will be outputted along side the password not accepted output.

How To Run:

1.Input IP address and password
2.A valid or invalid IP message will output depending on input, a password accepted or a password notn accepted and a random password will output depeding on the input, program ends.
