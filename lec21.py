def average (a=9, b=1):
    print("the average is ", (a+b)/2)
def average(*numebers):
    sum=0
    for i in numebers:
        sum = sum + i
        # print ("average is : ", sum/len(numebers))
       # return 7
    return sum/len(numebers)
        #average = (4,6)
    #average (b = 9)
    c = average(5,6,7,1)
    print(c)
    
    
   #average(b=9, a=21)
#def name(**name):
      # print(type(name))
      # print("hello,",name["fname"],
       #name["mname"], name["lname"])
       
       #name(mname = "buchanan", lname = "barnes", fname = "james")
       