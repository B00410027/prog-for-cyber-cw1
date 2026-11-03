#Securirty Event Logger
import random
from datetime import datetime
import socket


#variables
username = "username"
password = "password"

guess = False
while guess == False:
    print("---"*45)
    u_guess = input("Enter username: ") #Input username
    p_guess = input("Enter password: ") #Input password
    event_id = random.randint(1000,9999) #Creates random event ID
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Creates timestamp
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creates IP address
    s.connect(("8.8.8.8", 80)) 
    ip_address = s.getsockname()[0]
    s.close()
    if u_guess == "username" and p_guess == "password": #prints and breaks loop if "username" and "password" have been guessed
        print("---"*45)
        print(f"Event ID: {event_id}")
        print("Username: Admin")
        print(f"IP Address: {ip_address}")
        print("Event: Successful login")
        print(f"Timestamp: {timestamp}")
        break
    else: #Prints if "username" and/or "password" have not been guessed
        print("---"*45)
        print(f"Event ID: {event_id}")
        print("Username: Admin")
        print(f"IP Address: {ip_address}")
        print("Event: Failed login")
        print(f"Timestamp: {timestamp}")
