with open('sample.txt', 'w') as file:
    file.write("Hello, World!")
    # move to the 10th byte in the file
    file.seek(10)
    
    
# read the next 5 bytes
    print(file.read(5))
    
print("data")