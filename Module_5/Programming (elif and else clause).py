x = input("Enter a non-negative integer >")

try:
    n = int(x)

    if n >= 0:
        print(f"{n} * 2 is {n * 2}")
    else:
        print(f"{x} is not a non-negative integer")
        
except ValueError:
    print(f"{x} is not a non-negative integer")
