def coke_machine():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due: ", amount_due, sep="")
        coin = (input("Insert Coin: "))

        if coin.isdigit():
            coin = int(coin)
            if coin in [5,10,25]:
                amount_due -= coin

            else:
                print("Invalid coin. Please insert 5, 10, or 25 cents.")
        else:
            print("Invalid input. Please enter a number.")

    #if amount_due <= 0:
    print("Change Owed: " + str(abs(amount_due)))


if __name__ == "__main__":
    coke_machine()
