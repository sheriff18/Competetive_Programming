
from collections import Counter

shoes_number = int(input())
shoe_sizes_list = input().split()
customer_number = int(input())

dict_counter= Counter(map(int, shoe_sizes_list))
total_earned = []

for _ in range(customer_number):
    shoe_sizes_desired, price = map(int, tuple(input().split()))

    if shoe_sizes_desired in dict_counter.keys() and dict_counter[shoe_sizes_desired] >= 1:
        dict_counter[shoe_sizes_desired] -= 1
        total_earned.append(price)
        
print(sum(total_earned))
