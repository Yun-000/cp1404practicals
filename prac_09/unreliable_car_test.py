from prac_09.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Good Car", 100, 87.6)
    bad_car = UnreliableCar("Bad Car", 100, 20.3)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:13} drive {good_car.drive(i)}km")
        print(f"{bad_car.name:13} drive {bad_car.drive(i)}km")
        print()

    print(good_car)
    print(bad_car)


main()
