fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

index = 0

while index < len(fibonacci_sequence):

    user_input = int(input("Enter the next Fibonacci number >"))

    if user_input != fibonacci_sequence[index]:
        print("Try again")
        break
    
    index += 1
    
    if fibonacci_sequence[index - 1] > 50:
        print("Well done")
        break
else:
    print("Well done")