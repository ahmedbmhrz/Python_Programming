def append_fibonacci(integer_list):
    if len(integer_list) < 2:
        integer_list.append(1)
    else:
        new_element = integer_list[-1] + integer_list[-2]
        # Append the new element to the list
        integer_list.append(new_element)

def main():
    fib_list = [3, 5, 8]
    append_fibonacci(fib_list)
    print(fib_list)

main()
