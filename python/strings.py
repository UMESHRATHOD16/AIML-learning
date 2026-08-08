chai = "Masala chai"
print(chai)
first_char = chai[0]
print(first_char)
print(chai[0:6]) # slicing, last is not inclusive
nums = "0123456789"
print(nums[:])
print(nums[:7])
print(nums[3:])
print(nums[2:4])
print(nums[0:7:2]) # 2 means here hopping 2 = 1 hopping n = n-1 hoppings
print(nums[7:])
chai2 = "GinGer tea"
print(chai2.lower())
print(chai2.upper())

#strip and replace
chai3 = "  lemon tea  "
print(chai3)
print(chai3.strip()) # removes the trailing spaces
print(chai3.replace("lemon", "mint"))

#split 
chaii = "Giner, Mint, MAsala, Lemon"
chai_list = chaii.split(", ")
print(chai_list[1]) 

#find()
new_chai = "lemon tea"
print(new_chai.find("tea"))
print(new_chai.find("chai")) #gives -1 because its not present

#count()
chai4 = "ginger tea tea tea tea"
print(chai4.count("tea"))

#format --> we can put variables {in curly braces}
chai_type = "Masala tea"
quantity = 2
print("i ordered {} cups of {}".format(quantity,chai_type))

# List to String --> join

chai_variety = ["lemon", "masala", "ginger"]
print(" ".join(chai_variety))

# length of a string
print(len(chai_type))

#raw text (r"")
print(r"c:\pwd\users ") # back slashes are ignored due to raw