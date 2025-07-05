#Control Statements

num = 0

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is equal to zero")    
else:
    print("This number is negative")
    
num1 = int(input("Enter the first number:")) 
num2 = int(input("Enter the second number:"))   

if num1 > num2: 
   print(num1, "is greater than", num2)
elif num1 > num2:
   print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")   

#Loops

fruits = ["apple", "banana", "cherry"]     
for fruit in fruits:
    print(fruit)
    
count = 1 

while count <= 5:
    print(count)
    count += 1 
    
# Loop control statements

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        continue #Skips cherry and moves to the iteration
    print(fruit)    

print()

for fruit in fruits:
    if fruit == "cherry":
        pass #Placeholder, no action sis needed for cherry
    print(fruit)     
    
count = 0        
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  #Exits the loop when the count is reached - 3