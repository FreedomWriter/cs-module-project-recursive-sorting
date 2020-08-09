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

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
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

