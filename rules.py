from customers import rentals

def can_rent(lic):
    count = 0
    for r in rentals:
        if r["lic"] == lic:
            count = count + 1
    return count < 1