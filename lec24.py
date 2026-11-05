tup = (1,26,76,342,32,"green")
# tup[0] = 90
print(type(tup),tup)
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 342 in tup:
    print("yes 342 is present in the tuple")
tup2 = tup[1:4]
print(tup2)