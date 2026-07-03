print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >=18:
        print("you are can buy full tickets")

    elif age >=16:
        print("you are can buy short tickets")

    elif age >=8:
        print("you are can buy long tickets")
else:
    print("Sorry you have to grow taller before you can ride.")
