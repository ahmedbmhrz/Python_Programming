def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        integer_list.append(1)
    else:
        new_element = integer_list[-1] + integer_list[-2]
        integer_list.append(new_element)

def fibonacci(max):

    fib_list = []
    
    if max == 0:
        return fib_list

    while True:
        append_fibonacci(fib_list)
        if fib_list[-1] > max:
            fib_list.pop()
            break
            
    return fib_list

def main():

    user_input = input("Enter a non-negative integer >")
    
    if user_input.isdigit():
        n = int(user_input)
        fib_sequence = fibonacci(n)
        print("The Fibonacci series starts with:", fib_sequence)
    else:
        print(f"{user_input} is not a non-negative integer")

