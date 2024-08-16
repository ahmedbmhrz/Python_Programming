numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)

user_input = input("Enter an integer between 1 and 10 >")

if user_input.isdigit():
    num = int(user_input)
    
    if 1 <= num <= 10:
        numbers[num - 1] = 'gone'
        print(numbers)
    else:
        print(f"{num} is not between 1 and 10")
else:
    print(f"{user_input} is not a positive integer")
