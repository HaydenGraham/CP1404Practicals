log = open("name.txt", "r")
name = log.read().strip()
log.close()
print("Your name is " + name)
