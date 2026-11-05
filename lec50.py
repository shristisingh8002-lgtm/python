#f = open('myfile.txt', 'r')
#i = 0
#while True:
    #i= i+1
    #line = f.readline()
    #if not line:
        #break
   # m1 = int(line.split(',')[0])
   # m2 = int(line.split(',')[1])
   # m3 = int(line.split(',')[2])
    #print(f"marks of student 1: {m1}, marks of student 2: {m2}, marks of student 3: {m3}")
    #english = line.split(',')[3]
    #if not line:
        #break
    #print(line)
    
f= open('myfile2.txt', 'r') 
lines = ['line 1\n', 'line 2\n', 'line 3\n']  
f.writelines(lines)
f.close()



