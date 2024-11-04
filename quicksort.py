def profit_weight_ratio(item):
    profit,weight = item
    return profit / weight

def fractional_knapsack(items,capacity):
    total_profit=0
    items.sort(key = profit_weight_ratio, reverse = True)
    
    for profit,weight in items:
        if weight <= capacity:
            total_profit += profit
            capacity -= weight
        else:
            fraction = capacity/weight
            total_profit += profit * fraction
            break
    return total_profit

n=int(input("Enter number of items:- "))
items=[]

for i in range(n):
    profit = int(input(f"Enter the profit of {i+1}item: "))
    weight = int(input(f"Enter the weight of {i+1}item: "))
    items.append((profit,weight))

capacity = float(input("Enter the capacity:- "))

max_profit = fractional_knapsack(items,capacity)
print(f"Max profit in knapsack is {max_profit}")