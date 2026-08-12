print("==== MOVIE TICKET MENU ====")
age = int(input("Enter Your age: "))
day = "Wednesday"
price = 12 if age >= 18 else 8
if day == "Wednesday" :
    price = price - 2

print(f'price of you ticket is ${price}')