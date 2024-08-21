def largest_two(target_list):
    

    largest = max(target_list)
    
    list_copy = target_list.copy()
    list_copy.remove(largest)
    
    second_largest = max(list_copy)
    
    print(f"The largest and second largest elements in the list {target_list} are {largest} and {second_largest}")
    
largest_two([4, 2, 8, 7, 8])
