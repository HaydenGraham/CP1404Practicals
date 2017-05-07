from taxi import Taxi, UnreliableCar, SilverStarTaxi, Limo, Taxi
from random import randint


def main():
    bill_to_date = 0
    run = 1


    print("Let's Drive!")

    if bill_to_date > 0:
        print(bill_to_date)

    while run == 1:
        menuselection = input("q)uit, c)hoose taxi, d)rive")
        if menuselection == 'q':
            run = 0
        if menuselection == "c":
            car = choose_car()
        if menuselection == 'd':
            distance = int(input("Drive How far?"))
            bill_to_date += drive(car, distance)
            print("Your bill to date is: {}".format(bill_to_date))


def drive(car, distance):
    if car == 0:
        taxi = Taxi("Prius 1", 100)
        taxi.drive(distance)
        print("Your Prius trip costed you ${}".format(taxi.get_fare()))
        return taxi.get_fare()
    if car == 1:
        limo = Limo("Limo", 200, 2)
        limo.drive(10)
        print(limo)
        print("Current Fare: ${}".format(limo.get_fare()))
        return limo.get_fare()
    if car == 2:
        Hummer = SilverStarTaxi("Silver Star Hummer", 200, 2)
        Hummer.drive(10)
        print(Hummer)
        print("Current Fare: ${}".format(Hummer.get_fare()))
        return Hummer.get_fare()
    if car == 3:
        unreliable_car = UnreliableCar("ShitBox 1", 100, 30)
        unreliable_car.drive(40)
        print(unreliable_car)
        return 0


def choose_car():
    print("Taxis avalible:")
    print("0- {}".format(Taxi("Prius 1", 100)))
    print("0- {}".format(Limo("Limo", 100)))
    print("0- {}".format(SilverStarTaxi("Hummer", 100)))
    choice = int(input("Choose taxi: "))
    return choice


main()
