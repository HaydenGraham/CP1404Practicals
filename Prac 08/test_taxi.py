from taxi import Taxi, UnreliableCar, SilverStarTaxi, Limo, Taxi
from random import randint


def main():
    taxis = [Taxi("Prius 1", 100), Limo("Limo", 200, 2), SilverStarTaxi("Silver Star Hummer", 200, 2)]
    print("Let's Drive!")
    menuselection = menu()
    choice = menuselection
    print(choice)
    bill_to_date = 0
    while choice != 'q':
        if bill_to_date > 0:
            print(bill_to_date)
        if menuselection == "c":
            carnum = choose_car(taxis)
            print(taxis[carnum])
            car = taxis[carnum]
        elif menuselection == 'd':
            distance = int(input("Drive How far?"))
            car.drive(distance)
            bill_to_date += car.get_fare()
            print("Your bill to date is: {}".format(bill_to_date))
        menuselection = menu()
        choice = menuselection




def menu():
    menuselection = input("q)uit, c)hoose taxi, d)rive")
    return menuselection



def choose_car(taxis):
    print("Taxis avalible:")
    for taxi in taxis:
        print(taxi)
    choice = int(input("Choose taxi: "))
    return choice


main()
