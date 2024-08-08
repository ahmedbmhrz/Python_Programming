x = input("Enter an integer >")

try:
    n = int(x)

    print(f"The negative of {n} is {-n}")

except ValueError:

    print(f"{x} is not an integer")
