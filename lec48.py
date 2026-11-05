x = 10 # global variable
print(x)

def hello():
    x = 5 # local variable
    
    print(x)
    print("Hello, World!")
    
    hello()
    print(f"the global x is {x}") 
    x = 5
    print(f"the local x is {x}")
    
    "my_function"(x)
    print(x) # print 5
    # print(y) # this will raise an error because y is not defined in this scope