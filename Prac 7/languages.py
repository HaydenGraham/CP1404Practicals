from programminglanguage import ProgrammingLaunguage

def main():
    ruby = ProgrammingLaunguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLaunguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLaunguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(vb)
    list_of_software = []
    list_of_software.append(ruby)
    list_of_software.append(python)
    list_of_software.append(vb)
    print("The dynamically types languages are:")
    for item in list_of_software[1]:
        if item == "Dynamic":
            print(item)

main()