size = int(input("Enter the size of the pattern: "))
while size <= 0:
    print("Enter a positive Intager")
    size = int(input(" Enter the size of the pattern:"))
row =0 

while row < size:
    # use for loop for columns 
    for col in range(size):
        print("*", end="") # print stars on the same line
    print() # Move to the next line after a full row
    row= row + 1
     
