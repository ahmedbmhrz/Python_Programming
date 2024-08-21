import math

def stats():
    global my_list
    
    total = sum(my_list)
    mean = total / len(my_list)
    
    variance_sum = sum((x - mean) ** 2 for x in my_list)
    population_variance = variance_sum / len(my_list)
    population_std_dev = math.sqrt(population_variance)
    
    print(my_list)
    print(f"mean is {round(mean, 2)}")
    print(f"population standard deviation is {round(population_std_dev, 2)}")

my_list = [2, 4, 6, 8, 10, 12]
stats()
