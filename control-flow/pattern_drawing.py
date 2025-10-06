#initializing the variables
number = int(input("Enter the size of the pattern: "))

#main code to execute
i = 0
while number > i: #outer loop for rows
    j = 0
    while j < number: #inner loop for columns
        print("*", end="")
        j += 1
    print()
    i += 1
  