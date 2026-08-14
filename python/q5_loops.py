input_str = input("Enter the string: ")

for char in input_str :
    print(char)
    if input_str.count(char) == 1:
        print(f'The first repeating char is "{char}" ')
        break