from cars import fleet, show_cars, update_cars
from pricing import calculate_bill
from customers import rentals, add_rental, remove_rental
from rules import can_rent
from reports import LOW_LIMIT, NO_RENTALS, ALL_OK

while True:
    ch = input("\n1.Cars 2.Rent 3.Return 4.Active 5.Alerts 6.Exit\nChoice: ")

    if ch == "1":
        show_cars()

    elif ch == "2":
        car = input("Car: ")
        lic = input("License: ")
        if car in fleet and fleet[car] > 0 and can_rent(lic):
            days = int(input("Days: "))
            update_cars(car, -1)
            add_rental(lic, car, days)
            print("Rented! Total Bill: Rs.", calculate_bill(car, days))
        else:
            print("Car unavailable or license limit reached!")

    elif ch == "3":
        lic = input("License: ")
        car = input("Car: ")
        if remove_rental(lic, car):
            update_cars(car, 1)
            print("Returned successfully!")
        else:
            print("No matching record found!")

    elif ch == "4":
        if not rentals:
            print(NO_RENTALS)
        for r in rentals:
            print(r["lic"], "-", r["car"], "-", r["days"], "days")

    elif ch == "5":
        found = False
        for c in fleet:
            if fleet[c] < LOW_LIMIT:
                print("Low stock:", c)
                found = True
        if not found:
            print(ALL_OK)

    elif ch == "6":
        print("Thankyou For Choosing Us!")
        break