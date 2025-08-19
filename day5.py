def find_leaders(arr):
    
    n = len(arr)
    if n == 0:
        return []

    leaders = []
    max_from_right = arr[n - 1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    leaders.reverse()
    return leaders

arr = [16, 17, 4, 3, 5, 2]
result = find_leaders(arr)
print(f"The leaders in the array {arr} are: {result}")

arr2 = [1, 2, 3, 4, 5]
result2 = find_leaders(arr2)
print(f"The leaders in the array {arr2} are: {result2}")

arr3 = [5, 4, 3, 2, 1]
result3 = find_leaders(arr3)
print(f"The leaders in the array {arr3} are: {result3}")
