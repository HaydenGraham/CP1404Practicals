from car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    limo = Car(100)
    limo.fuel += 20
    limo.drive(115)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print("odo =", limo.odometer)
    print(bus)


main()