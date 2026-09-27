def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("END")
    return wrapper

@decorator
def dec_fun():
    print("Thi function is used @ to go in decorator")

dec_fun()


""" 
    This Code tells us how a basic decorator works 
    @ is used like above the function where you need that function in you decorator function
    by simply calling the function name works !
"""