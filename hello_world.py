print('Hellow World!')

def chai(n):
    print(n)

chai("a")

chai_one = "lemon tea"
chai_two = "ginger tea"
chai_three = "masala tea"



# Python shell commands 

# "ModuleNotFoundError: No module named 'chai.py'; 'chai' is not a package
# >>> import hello_world
# >>> hello_world.chai("mint tea")
# mint tea
# >>> reload(hello_world)
# Hellow World!
# a
# <module 'hello_world' from '/Users/rathodumesh/Desktop/VS CODE/Python/hello_world.py'>
# >>> chai(chai_one)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     chai(chai_one)
#     ^^^^
# NameError: name 'chai' is not defined
# >>> hello_world.chai(chai_one)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     hello_world.chai(chai_one)
#                      ^^^^^^^^
# NameError: name 'chai_one' is not defined
# >>> hello_world.chai("chai_one")
# chai_one
# >>> chai_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     chai_one
# NameError: name 'chai_one' is not defined
# >>> hello_world.chai_one
# 'lemon tea'
# >>> hello_world.chai_three
# 'masala tea'