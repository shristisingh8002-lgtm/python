def func():
  try:
    l = [ 1, 5, 6, 7]
    l = int(input("enter the index:"))
    print[(l)]
  except:
    print("some error occured")
    
  finally:
    print("I am always exceuted")
#print("finally i am excecuted")

x = func()
print(x)