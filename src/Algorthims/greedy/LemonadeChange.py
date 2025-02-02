def lemonadeChange(bills) -> bool:
    
    # Store the count of $5 and $10 bills (we don’t need to track $20 bills)
    five, ten = 0, 0

    for bill in bills:
        if bill == 5:
            five += 1  # Accept the $5 bill

        elif bill == 10:
            if five > 0:
                five -= 1  # Give one $5 as change
                ten += 1   # Store one $10 bill
            else:
                return False  # Not enough $5 bills to give change

        else:  # bill == 20
            if ten > 0 and five > 0:  # Prefer giving one $10 and one $5
                ten -= 1
                five -= 1
            elif five >= 3:  # Otherwise, give three $5 bills
                five -= 3
            else:
                return False  # Not enough change

    return True 

bills = [5,5,5,10,20]
print(lemonadeChange(bills))