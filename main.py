import security_tools

ip_addr = input("Enter IP Address >> ") #User inputs IP address
passwd = input("Enter password >> ") #User inputs password
print("---"*45)

security_tools.val_ip(ip_addr) #Function called using "ip_addr" as perametor
security_tools.val_pass(passwd) #Function called using "passwd" as a peramtor, function "rand_pass()" will be called if "passwd" input isnt valid
