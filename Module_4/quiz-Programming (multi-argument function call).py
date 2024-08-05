import math

x = int(input("Enter an integer >"))
y = int(input("Enter an integer >"))

a = math.pow(x,y)

b = math.pow(y,x)

print(f"{x} to the power of {y} is {int(a)}")

print(f"{y} to the power of {x} is {int(b)}")

maxInt = max(a,b)

print(f"the max of {int(a)} and {int(b)} is {int(maxInt)}")