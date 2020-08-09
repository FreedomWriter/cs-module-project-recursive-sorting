# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Your code here
    middle = 0

    while start <= end:
        middle = start + end // 2
        try:
            if arr[middle] > target:
                return binary_search(arr, target, start, middle-1)
            else:
                return arr.index(target)
        except:
            return -1
        
    return -1  # not found  

# def binary_search(arr, target, start, end):
#     # Your code here
#     if len(arr) == 0:
#         return -1

#     middle = 0
#     while start <= end:
#         middle = start + end // 2
#         if arr[middle] > target:
#             return binary_search(arr, target, start, middle-1)
#         elif arr[middle] < target:
#             return binary_search(arr, target, middle+1, end)
#         elif arr[middle] == target:
#             return middle 
        
#     if middle > start:
#         return middle
#     else:
#         return -1

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []

print(binary_search(arr1, -8, 0, len(arr1)-1))        
print(binary_search(arr1, 10, 0, len(arr1)-1))
print(binary_search(arr1, 1, 0, len(arr1)-1))
print(binary_search(arr2, 6, 0, len(arr2)-1))
print(binary_search(arr2, 0, 0, len(arr2)-1))
# 


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # if len(arr) == 0:
    #     return -1
    
    # Your code here
    start = 0
    middle = 0
    end = len(arr) -1



    while start <= end:
        middle = start + end // 2
        try:
            if arr[middle] > target:
                if arr[middle] > arr[middle -1]:
                    return binary_search(arr, target, start, middle-1)
                else:
                    return binary_search(arr, target,  middle-1, end)
            else:
                return arr.index(target)
        except:
            return -1
        
    return -1  # not found  

