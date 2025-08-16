def find_missing_number_sum(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
my_array = [1, 2, 4, 5]
missing_sum = find_missing_number_sum(my_array)
print(f"The missing number is {missing_sum}") # Output: 3
