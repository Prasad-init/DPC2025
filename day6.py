from collections import defaultdict

def find_zero_sum_subarrays(arr):
    sum_map = defaultdict(list)
    result = []
    current_sum = 0
    sum_map[0].append(-1)
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum in sum_map:
            for start_index in sum_map[current_sum]:
                result.append((start_index + 1, i))
        sum_map[current_sum].append(i)
    return result

input_arr = [1, 2, -3, 3, -1, 2]
output = find_zero_sum_subarrays(input_arr)
print(f"Input: {input_arr}")
print(f"Output: {output}")

input_arr_2 = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
output_2 = find_zero_sum_subarrays(input_arr_2)
print(f"\nInput: {input_arr_2}")
print(f"Output: {output_2}")
