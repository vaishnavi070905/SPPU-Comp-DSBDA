n = int(input("Enter number of elements: "))

items = []

for i in range(n):
    p = int(input(f"Enter profit for Item {i+1}: "))
    w = int(input(f"Enter weight for Item {i+1}: "))
    items.append((i+1, p, w, p/w))

capacity = int(input("Enter the Knapsack Capacity: "))

# Sort according to profit/weight ratio
items.sort(key=lambda x: x[3], reverse=True)

total_profit = 0

for i, p, w, r in items:

    if capacity == 0:
        break

    if w <= capacity:
        capacity -= w
        total_profit += p

        print(f"Item {i} taken Fully (Weight = {w}, Profit = {p})")

    else:
        fraction = capacity / w
        total_profit += fraction * p

        print(
            f"Item {i} taken {round(fraction*100, 2)}%"
            f" | Weight taken = {capacity}"
            f" | Profit taken = {round(fraction*p, 2)}"
        )

        capacity = 0

print("Total Maximum Profit:", round(total_profit, 2))
