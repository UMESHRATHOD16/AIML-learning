age = int(input("Enter age to categorise age group : "))
if(age < 13) :
    print("Child Category")
elif(age>=13 and age <=19):
    print("Teenage Categpry")
elif(age>=20 and age <=59):
    print("Adult Categpry")
else:
    print("senior Category")