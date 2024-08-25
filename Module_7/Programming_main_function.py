def string_lengths(string_list):
    lengths_list = [len(string) for string in string_list]

    print(string_list)
    print(lengths_list)

def main():
    words = input("Enter some words >").split()

    string_lengths(words)

main()
