import time
import random
from algorithm import recursive_binary_search, iterative_binary_search, sequential_search

dataSize = [ 5000, 50000, 100000, 150000, 1000000]

print("Measuring Runtime Growth:")

for N in dataSize:
    SumRBS = 0
    SumIBS = 0
    SumSS = 0

    for _ in range(10):
        arr = sorted([random.randint(1, 1000000) for _ in range(N)])
        target = random.randint(1, 1000000)

        start = time.perf_counter()
        recursive_binary_search(arr, target, 0, len(arr) - 1)
        SumRBS += (time.perf_counter() - start) * 1000000

        start = time.perf_counter()
        iterative_binary_search(arr, target)
        SumIBS += (time.perf_counter() - start) * 1000000

        start = time.perf_counter()
        sequential_search(arr, target)
        SumSS += (time.perf_counter() - start) * 1000000

    print(f"Data Size: {N}")
    print(f"  Recursive Binary Search Average Time: {SumRBS / 10:.2f} µs")
    print(f"  Iterative Binary Search Average Time: {SumIBS / 10:.2f} µs")
    print(f"  Sequential Search Average Time: {SumSS / 10:.2f} µs")
    print()