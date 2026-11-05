info = {"name " : "karan", "age" : 20, "eligible": True}
#print(info)
#print(info.keys())

#for key in info.keys():
    #print(f"the value corresponding to the key {key} is {info[key]}")
    
print(info.items())
for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")