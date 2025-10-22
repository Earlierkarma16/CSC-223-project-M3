import random 
from algorithm import recursive_binary_search, iterative_binary_search, sequential_search

arr = [random.randint(1, 100) for _ in range(20)]
target = random.choice(arr) if random.random() < 0.5 else 999

arr.sort()
print(f"Array: {arr}")
print(f"Target: {target}")

print("Recursive Binary Search:")
result_rbs = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"Target found at index: (RBS): {result_rbs}")
print("Iterative Binary Search:")
result_ibs = iterative_binary_search(arr, target)
print(f"Target found at index (IBS): {result_ibs}")

print("Sequential Search:")
result_ss = sequential_search(arr, target)
print(f"Target found at index (SS): {result_ss}")