def main():
    additems("Item: ")

def additems(prompt):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    totalprice = 0

    while True:
        try:
            itemtoadd = input(prompt).title()
            if itemtoadd in menu:
                totalprice = totalprice + menu[itemtoadd]

        except EOFError:
            break

        else:
            print("Total: ", totalprice)

main()