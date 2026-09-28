prices = {"Sedan": 1500, "SUV": 2500, "Hatchback": 1000}

def calculate_bill(car, days):
    if car in prices:
        return prices[car] * days
    return 0