# Manages the car fleet inventory and updates the number of cars along with their types available
fleet = {"Sedan": 10, "SUV": 15, "Hatchback": 10}

def show_cars():
    for car in fleet:
        print(car, ":", fleet[car], "left")

def update_cars(car, change):
    if car in fleet:
        fleet[car] = fleet[car] + change