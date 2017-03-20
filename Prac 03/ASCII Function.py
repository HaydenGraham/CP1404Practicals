LOWER = "33"
UPPER = "127"


def main():
    get_number(UPPER, LOWER)
    get_letter()


def get_number(UPPER, LOWER):
    try:
        number_recieved = int(input("Enter a number({}-{})".format(LOWER, UPPER)))
        while int(UPPER) < number_recieved or number_recieved < int(LOWER):
            number_recieved = int(input("Enter a valid number({}-{})".format(LOWER, UPPER)))
    except ValueError:
        print("Please enter a valid number!")
        get_number(UPPER, LOWER)


def get_letter():
    try:
        letter_to_number = str(input("Enter a character: "))
        print("The ASCII code for {} is {}".format(letter_to_number, ord(letter_to_number)))
    except TypeError:
        print("Please enter a valid letter!")
        get_letter()


main()


