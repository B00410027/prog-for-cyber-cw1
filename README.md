Branch Security Tool 

Student Details:
Name - Shaun McFadzean
Banner ID - B00410027
Campus - Lanarkshire

Program:
This python program will make the user navigate a menu with 4 options. The options are 1. Security Event Counter, 2. Brute Force Simulation, 3. Login Authentication, 4. Exit.
1. Security Event Counter
   The user will be prompted to guess the password 10 times. After the 10 attempts a security alert will output depending on the percentage of incorrect guesses.
2. Brute Force Simulation
   The user will be prompted to guess the password. They have 5 attempts. A message will output depending on the user input.
3. Login Authentication
   The user will be prompted to guess the username and password. They have 3 attempts. Authentication is only successful is both username and password are guessed correctly.
4. Exit
   The user will exit the program.

Code:
1. The user will input their password guess, if correct +1 will be added to the correct_count and +1 to incorrect_count if the guess is incorrect. Once all 10 guesses have been made, the program will take the incorrect_count and convert it to a percentage. If the percentage is greater than 50% then the security alert will output, if the percentage is 50% or less, a standard message will output.

2. The user will input their password guess. If correct, a successful message will be outputted and the program will end. If incorrect, +1 will be added to count and an incorrect  message will be outputted, the user will then be prompted again until either a successful input or count = 5, after which a maximum attempts used message will be outputted and the program will end.

3. The user will input their username and password guess, after both have been inputted +1 will be added to guess. If both inputs are correct a successful authentication message will be outputted. If either or/and both of the inputs are incorrect then a failed authentication message will be outputted. The user will then be prompted again and will be until guess = 4 (3 guesses total) where a max attempts message will be outputted or successful inputs.

4. Thank you message outputted, end of program.

How To Use:
1. Run code.
2. Input either 1, 2, 3 or 4.
   
3.1. If input = 1, enter password 10 times, output message, program ends.

3.2. If input = 2, enter password up until correct or up to 5 guesses have been used, output message, program ends.

3.3. If input = 3, enter username and password until correct or up to 3 guesses have been used, output message, program ends.

3.4. If input = 4, output message, program ends.
