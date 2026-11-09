#Security Incident Manager Using Dictionaries

incident = {"Username": "B00410027", "IP": "192.168.10.3", "Event type": "Failed login", "Risk level": "Medium"} #Create dictionary
print(incident) #Print original dictionary
print("---"*50)
print(f"Username: {incident['Username']}\nIP Address: {incident['IP']}") #Print username and password
incident["Status"] = "Down" #Create new key : value pair
incident["Risk level"] = "Low" #Edit Risk Level value to low
del incident["Username"] #Delete key "username" and value "B00410027"
print("---"*50)
print(f"All remaining Key : Value pairs\n{incident}") #Print all remaining key :value pairs
print("---"*50)
print(f"Total number of Key : Value pairs left: {len(incident)}") #Prints total number of key value pairs