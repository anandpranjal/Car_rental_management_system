rentals = []

def add_rental(lic, car, days):
    rentals.append({"lic": lic, "car": car, "days": days})

def remove_rental(lic, car):
    for r in rentals:
        if r["lic"] == lic and r["car"] == car:
            rentals.remove(r)
            return True
    return False