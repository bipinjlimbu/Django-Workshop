#Sum of first 10 natural numbers
sum = 0
for i in range(1,11,):
    sum += i

print("The sum is:", sum)

print("Using While Loop")
sum = 0
i = 0
while(i<=10):
    sum += i
    i += 1

print("The sum is:", sum)

#Multiplication Table
print("Multiplication Table of 8")
n = 8
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

print("Using While Loop")   
i = 1
while(i<=10):
    print(f"{n} x {i} = {n*i}")
    i += 1

#Print Even Numbers between 1 to 10
sum = 0
for i in range(2,11,2):
    sum += i

print("The sum of Even Numbers is:", sum) 

sum = 0
for i in range(1,10,2):
    sum += i

print("The sum of Odd Numbers is:", sum)

even = []
odd = []
print("Using While Loop")
i = 1
while(i<=10):
    if i%2 == 0:
        even.append(i)

    else:
        odd.append(i)
    i += 1

print("Even Numbers are:", even)
print("Odd Numbers are:", odd)

n = int(input("Enter Any Number:"))
count = 0
for i in range(1,n+1):
    if n==0 or n==1:
        break
    if n%i == 0:
        count += 1

if count == 2:
    print(f"{n} is a Prime Number")

else:
    print(f"{n} is not a Prime Number")