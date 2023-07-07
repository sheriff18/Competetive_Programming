

from collections import OrderedDict

N = int(input())
sales = OrderedDict()

for i in range(N):
    #reversed split for the last space.
    item_name, item_price = input().rsplit(" ", 1)  
    sales[item_name] = sales.get(item_name,0)
    sales[item_name] += int(item_price)
    
for item_name, net_price in sales.items():
    print(f"{item_name} {net_price}")
