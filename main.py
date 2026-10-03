print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below.\n")
print("Options: \n1 - Length\n2 - Weight\n0 - Exit")
option=input("Your choice: ")
if option=="1":
    print("\nLength options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    sub_option=input("Your choice:")
    if sub_option=="1":
        meters=float(input("Insert meters:"))
        kilometers=meters/1000
        kilometers=round(kilometers, 1)
        print(f"{meters} m is {kilometers} km")
    elif sub_option=="2":
        kilometers=float(input("Insert kilometers:"))
        meters=kilometers*1000
        meters=round(meters, 1)
        print(f"{kilometers} km is {meters} m) ")
    elif sub_option=="0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif option=="2":
    print("\nWeight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    sub_option=input("Your choice:")
    if sub_option=="1":
        grams=float(input("Insert grams:"))
        pounds=grams*0.00220462
        pounds=round(pounds, 1)
        print(f"{grams} g is {pounds} lb")
    elif sub_option=="2":
        pounds=float(input("Insert pounds:"))
        grams=pounds*453.59237
        grams=round(grams, 1)
        print(f"{pounds} lb is {grams} g")
    elif sub_option=="0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif option=="0":
    print("Exiting...")
else:
    print("Unknown option.")
print(f"\nProgram ending.")



 

