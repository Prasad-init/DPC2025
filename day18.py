import math

def count_divisors(n):
    if n <= 0:
        return 0
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                count += 1
            else:
                count += 2
    return count

N = 12
result = count_divisors(N)
print(f"Input: {N}")
print(f"Output: {result}")

N = 36
result = count_divisors(N)
print(f"Input: {N}")
print(f"Output: {result}")
