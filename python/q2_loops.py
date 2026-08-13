number = int(input("Enter a number: "))
sum = 0
for num in range(number+1):
    if(num%2 == 0):
        sum = sum + num

print(f'The Sum of Even numbers till {number} is {sum}')