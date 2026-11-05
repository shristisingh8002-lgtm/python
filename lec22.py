marks =[3, 5, 6,"harry", True , 6,7 ,2,32,345,23]  
#print(marks)
#print(type(marks))
#print(marks[0])
#print(marks[1])
#print(marks[2])
#print(marks[3])

#print(marks[-3])# negative index
#print(marks[len(marks)-3])#positive index
#print(marks[5-3]) # positive index
#print(marks[2])# positive index

if "6" in marks:
    print("yes")
else:
  #print("no")
  # same thing applies for string as well  
    #if "ha" in harry:
      #  print("yes")
  print(marks)
  
#print(marks[0:7])      
#print(marks[1:9]) 
#print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)