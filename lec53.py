# MAP
#def cube (x):
    #return x ** 3

#print(cube(2))

# l = (1,2,4,6,4,3)

#new_l = []
# for item in l:
# newl. append(cube(item))

#newl = list(map(lambda x: x ** 3, l))

#print(newl)

#def filter_function(a):
    #return a > 2

#newl = list(filter(filter_function, l))
#print(newl)

from functools import reduce

# list of numbers
numbers = [1, 2, 3, 4, 5]


# calculate the sum of numbers using reduce function
def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)

# print the sum 
print(sum)
