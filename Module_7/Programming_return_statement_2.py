def as_integer(an_object):
    if isinstance(an_object, str):
        if an_object.lstrip('-').isdigit():
            return int(an_object)
    return None

def filter_ints(word_list):
    int_list = []
    error_list = []

    for word in word_list:
        integer = as_integer(word)
        if integer is not None:
            int_list.append(integer)
        else:
            error_list.append(word)

    return (int_list, error_list)

def main():
    user_input = input("Enter some integers >")

    word_list = user_input.split()

    valid_ints, errors = filter_ints(word_list)

    print(f"The sum of: {valid_ints} is {sum(valid_ints)}")

    if errors:
        print(f"These words are not integers: {errors}")

main()
