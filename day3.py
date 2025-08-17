from typing import List

def findDuplicate(arr: List[int]) -> int:
    tortoise = arr[0]
    hare = arr[0]
    
    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break
            
    p1 = arr[0]
    p2 = tortoise
    
    while p1 != p2:
        p1 = arr[p1]
        p2 = arr[p2]
        
    return p1

arr1 = [3, 1, 3, 4, 2]
duplicate1 = findDuplicate(arr1)
print(f"The array is: {arr1}")
print(f"The duplicate number is: {duplicate1}") # Expected output: 3

print("-" * 30)

arr2 = [1, 3, 4, 2, 2]
duplicate2 = findDuplicate(arr2)
print(f"The array is: {arr2}")
print(f"The duplicate number is: {duplicate2}") # Expected output: 2
