def main():
    nutritionlookup()

def nutritionlookup():
    nutrition = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50
    }
    
    item = input("Item: ").title()

    if item in nutrition:
        print("Calories: ", nutrition[item])
    else:
        print("We don't have that item info")
        
main()