tea_types = ("black","green","oolong")
tea_types
('black', 'green', 'oolong')
tea_types[1:]
('green', 'oolong')
tea_types[-1]
'oolong'
len(tea_types)
3
# we can assign varibales to tuples
(Black,Green,Oolong) = tea_types
Black
'black'
Green
'green'
Oolong
'oolong'
# here we assignnd varibales to the tuple tea_types wwhich both should contain equal values
type(tea_types)
<class 'tuple'>