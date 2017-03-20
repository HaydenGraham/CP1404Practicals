""" Hayden """
def main():

    get_name()


def get_name():
    try:
     name = str(input("Insert name:   "))
     while len(name) == 0:
         name = input("Insert name:  ")
     freq = int(input("What frequency of letters would you like to print? "))
     loop(name,freq)
    except ValueError:
        print("Enter a valid number")


def loop(name,freq):
    for i in range(0, len(name), freq):
        print(name[i])


main()
