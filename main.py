def main():

    not_paid = True
    owed = 50
    while not_paid:
        print(f"Amount Due: {owed}")
        paying_amount = int(input("Insert Coin: "))
        match paying_amount:
            case 25:
                owed -= paying_amount
            case 10:
                owed -= paying_amount
            case 5:
                owed -= paying_amount
            case _:
                pass
        if owed > 0:
            pass
        elif owed == 0:
            print(f"Change Owed: {owed}")
            not_paid = False
        else:
            owed *= -1
            print(f"Change Owed: {owed}")
            not_paid = False

main()