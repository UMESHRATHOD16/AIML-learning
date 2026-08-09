tea_varities = ["Black","white","oolong","green"]
print(tea_varities[0])
print(tea_varities[1])
print(tea_varities[-1]) #last element

# Slicing and dicing is also allowed in lists and also hopping([0:0:1])

tea_varities[3] = "Herbal"
print(tea_varities)
tea_varities[1:2] = ["lemon"]
print(tea_varities)
tea_varities[1:3] = ["lemon","masala"]
print(tea_varities) # ['Black', 'lemon', 'masala', 'Herbal']

print(tea_varities[1:1]) 
tea_varities[1:1] = ["test","test"] # it inserts the test test starting at 1 position
print(tea_varities)
tea_varities[0:2] = []
print(tea_varities)


# for in loop thaught 
# conditional if
if "oolong" in tea_varities:
    print("I have oolong tea") # it dont have it so it wont print this

tea_varities.append("oolong")

if "oolong" in tea_varities:
    print("I have oolong tea")

print(tea_varities)
tea_varities.pop()  # deletes the last value
print(tea_varities)
tea_varities.remove("Herbal")
print(tea_varities) # deletes the value given

# tea_varities_copy = tea_varities ## this creates just a reference, but if we need a real copy and create a new same list we need to use .copy

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)
tea_varities_copy.append("oolong")
print(tea_varities)
print(tea_varities_copy)

#list comprehension 

squared_nums_0 = [x**2 for x in range(1,11)]
print(squared_nums_0)
squared_nums_1 = [x**2 for x in range(10)] 
print(squared_nums_1)

# range works like slicing only, 1st number is inclusive and last in not and if 1st is not given then it takes from 0
