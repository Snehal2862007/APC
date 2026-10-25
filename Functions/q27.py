def consultation():
    return 500

def laboratory():
    return 1000

def medicine():
    return 800

def room(days):
    return days * 1500

def final_bill(days, category):
    total = consultation() + laboratory() + medicine() + room(days)
    if category == "senior":
        total *= 0.90
    elif category == "staff":
        total *= 0.80
    return total

print(final_bill(3, "senior"))