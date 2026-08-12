chai_types = {"Masala":"spicy","ginger":"zesty","green":"mild"}
print(chai_types)
print(chai_types["Masala"])
chai_types.get("ginger")
chai_types.get("gingery")   # get method handles error


chai_types = {"Masala":"spicy","ginger":"zesty","green":"mild"}
print(chai_types)
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
print(chai_types["Masala"])
spicy
chai_types.get("ginger")
'zesty'
chai_types.get("gingery")
chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
chai_types["green"] = "fresh"
chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh'}
for chai in chai_types:
         print(chai)
    
Masala
ginger
green
for chai in chai_types:
         print(chai, chai_types[chai])
    
Masala spicy
ginger zesty
green fresh
for key,value in chai_types.items():
         print(key,value)
    
Masala spicy
ginger zesty
green fresh
if "Masala" in chai
chai       chai_types
if "Masala" in chai_types:
         print("I have masala tea")
    
I have masala tea
if "Masalaaaa" in chai_types"
  File "<stdin>", line 1
    if "Masalaaaa" in chai_types"
                                ^
SyntaxError: unterminated string literal (detected at line 1)
if "Masalaaaa" in chai_types:
         print("I have masalaaa chai")
    
print(len(chai_types))
3
chai_types["newChai"] = "newFlavour"
chai
chai       chai_types
chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh', 'newChai': 'newFlavour'}
chai_types.pop("newChai")
'newFlavour'
chai_types
{'Masala': 'spicy', 'ginger': 'zesty', 'green': 'fresh'}
chai_types.popitem()
('green', 'fresh')
chai_types
{'Masala': 'spicy', 'ginger': 'zesty'}
del chai_types["ginger"]
chai_types
{'Masala': 'spicy'}
chai_types_copy = chai_types.copy()
chai_types_copy
{'Masala': 'spicy'}
chai_types_copy["Oolong"] = "sweet"
chai_types_copy
{'Masala': 'spicy', 'Oolong': 'sweet'}
chai_types
{'Masala': 'spicy'}
tea_shop = {
     "chai" : {"Masala":"Spicy","Ginger":"Zesty"},
     "Tea" : {"green":"Mild","black":"strong"}
     }
tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'green': 'Mild', 'black': 'strong'}}
tea_shop[chai][ginger]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_shop[chai][ginger]
    ~~~~~~~~^^^^^^
KeyError: 'green'
tea_shop["chai"]["ginger"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_shop["chai"]["ginger"]
    ~~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: 'ginger'
tea_shop["chai"]["Ginger"]
'Zesty'
tea_shop[chai][Ginger]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_shop[chai][Ginger]
    ~~~~~~~~^^^^^^
KeyError: 'green'
tea_shop["chai"]["Ginger"]
'Zesty'
squared_nums  = {x: x**2 for x in range(6)}
squared_nums
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squared_nums.clear()
squared_nums
{}
keys = ["masala","ginger","green"]
default_value = "delicious"
new_dict = dict.keysfrom(keys,def
def           default_value
new_dict = dict.keysfrom(keys,default_value)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    new_dict = dict.keysfrom(keys,default_value)
               ^^^^^^^^^^^^^
AttributeError: type object 'dict' has no attribute 'keysfrom'
new_dict = dict.fromkeys(keys,default_value)
new_dict
{'masala': 'delicious', 'ginger': 'delicious', 'green': 'delicious'}
values = ["spicy","zesty","mild"]
new_dict.clear()
new_dict
{}
neww_dict = dict.fromkeys(keys,for i in values range(3))
  File "<stdin>", line 1
    neww_dict = dict.fromkeys(keys,for i in values range(3))
                                   ^^^
SyntaxError: invalid syntax
