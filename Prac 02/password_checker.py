MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your  {} character password is valid:  {}".format(len(password), str(password)))


def is_valid_password(password):
    if len(password) > MAX_LENGTH:
        print('False')
        return False
    elif len(password) < MIN_LENGTH:
        print('False')
        return False
    else:
        print("Length good")

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for j in range(0, len(password)):
        if password[j].islower():
            count_lower += 1
        elif password[j].isupper():
            count_upper += 1
        elif password[j].isdigit():
            count_digit += 1
        # if password[j] in SPECIAL_CHARACTERS
# Checking for special characters separately

    for j in range(0, len(password)):
        for k in range(0, len(SPECIAL_CHARACTERS)):
            if password[j] == SPECIAL_CHARACTERS[k]:
                count_special += 1
    print(count_lower)
    print(count_upper)
    print(count_digit)
    print(count_special)
    if count_upper < 1 and count_digit < 1 and count_lower > 1:
    # if count_upper >= 1 and count_upper >= 1 and count_lower >= 1:
        if not SPECIAL_CHARACTERS:
            if count_special < 1:
                return False
    else:
        return False
        # if we get here (without having returned False), then the password must be valid
    return True


main()
