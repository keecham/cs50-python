while True:
    try:
        n = int(input("What's n?"))
        if n > 0:
         break
    except ValueError:
        print("Please enter a whole number")

for i in range(n):
    print("meow")