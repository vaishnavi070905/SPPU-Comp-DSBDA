n = int(input("Enter number of items: "))

items = []

for i in range(n):
    p = int(input("Enter profit for item " + str(i+1) + ": "))
    w = int(input("Enter weight for item " + str(i+1) + ": "))
    items.append((i+1, p, w, p/w))

capacity = int(input("Enter knapsack capacity: "))

# Sort by profit/weight ratio
items.sort(key=lambda x: x[3], reverse=True)

total_profit = 0

for i, p, w, r in items:
    if capacity == 0:
        break

    if w <= capacity:
        fraction = 1
        total_profit += p
        capacity -= w
        print("Item", i, "Taken Fully (Weight =", w, ", Profit =", p, ")")

    else:
        fraction = capacity / w
        used_weight = capacity
        profit = p * fraction
        total_profit += profit

        print("Item", i, "Taken:", round(fraction * 100, 2),
              "% (Weight =", used_weight,
              ", Profit =", round(profit, 2), ")")

        capacity = 0

print("Maximum Profit:", round(total_profit, 2))
