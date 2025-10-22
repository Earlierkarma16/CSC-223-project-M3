
import algorithm
from algorithm import recursive_binary_search, iterative_binary_search, sequential_search 

arr = [3, 5, 8, 12, 14, 18, 21]
arr.sort()
target1 = 12
target2 = 9

print("Testing Recursive Binary Search:")
index1 = recusive_binary_search(arr, target1, 0, len(arr) - 1)
print(f"{target1} found at index: {index1}" if index1 != -1 else f"{target1} not found")
index2 = recusive_binary_search(arr, target2, 0, len(arr) - 1)
print(f"{target2} found at index: {index2}" if index2 != -1 else f"{target2} not found")

print("\nTesting Iterative Binary Search:")
index1 = iterative_binary_search(arr, target1)
print(f"{target1} found at index: {index1}" if index1 != -1 else f"{target1} not found")
index2 = iterative_binary_search(arr, target2)
print(f"{target2} found at index: {index2}" if index2 != -1 else f"{target2} not found")

print("\nTesting Sequential Search:")
index1 = sequential_search(arr, target1)
print(f"{target1} found at index: {index1}" if index1 != -1 else f"{target1} not found")
index2 = sequential_search(arr, target2)
print(f"{target2} found at index: {index2}" if index2 != -1 else f"{target2} not found")
print("-"*20)
