# Numbers in python are very important
x = 2
y = 3
z = 4

print(x+y) # it gives 
x + y * z # avoid this
print ((x + y)*z) # use parantheses

print(40 + 2.3) # try to avoid this type, use same data types in opn

print( float(40) + 2.3 ) # like this

## operators 

print(x < y < z) # gives true but its confusing 
# its actually x<y(true) and y<z(true) = final and true

print(1==2<3) ## this is 1==2 and 2<3 so 1==2 fails so overall fails

## random lib 

import random 

print(random.randint(1,10))
print(random.randint(1,100))


l1 = ['ginger', 'masala', 'lemon', 'mint']
print(random.choice(l1))
print(random.shuffle(l1))