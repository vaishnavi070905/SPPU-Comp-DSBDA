
import time

# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Non-Recursive Fibonacci
def fib_non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

# Main Program
n = int(input("Enter number of terms: "))

# Recursive Fibonacci
print("\nFibonacci Sequence (Recursive): ", end="")

start1 = time.perf_counter()

for i in range(n):
    print(fib_recursive(i), end=" ")

end1 = time.perf_counter()

time_recursive = (end1 - start1) * 1000000

# Non-Recursive Fibonacci
print("\n\nFibonacci Sequence (Non-Recursive): ", end="")

start2 = time.perf_counter()

fib_non_recursive(n)

end2 = time.perf_counter()

time_nonrecursive = (end2 - start2) * 1000000

# Time and Space Complexity Analysis
print("\n\n=== Time and Space Complexity Analysis ===")

print("Recursive Time Taken:", round(time_recursive, 2), "microseconds")
print("Recursive Time Complexity: O(2^n)")
print("Recursive Space Complexity: O(n)")

print("\nNon-Recursive Time Taken:", round(time_nonrecursive, 2), "microseconds")
print("Non-Recursive Time Complexity: O(n)")
print("Non-Recursive Space Complexity: O(1)")
