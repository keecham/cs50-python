def main():
    coinchecker()


def coinchecker():
    amountdue = 50
    while (amountdue != 0):
        coin = int(input("Insert coin: "))
        if coin in [5, 10, 25]:
            amountdue = amountdue - coin
            if amountdue < 0:
                print("Change owed: ", 0 - amountdue)
                break
            else:
                print("Amount due: ", amountdue)
        else:
            print("That's not a valid coin")

main()