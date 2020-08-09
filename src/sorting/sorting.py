# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# print(merge([1,2,3], ['a', 'b', 'c']))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

import time
# [5,9,3,7,2,8,1,6]
# Chose a pivot
    # take first number in list - 5
# Move all elements smaller than pivot, to the left of the pivot
# Move all elements larger than pivot, to the right of pivot
# [3,2,1][5][9,7,8,9]
# Repeat the process on the two new arrays (left and right) - the pivot is where it's supposed to be
# arrays of one are the base case - they are sorted
    # each recursive call get the arrays they return combined and then returned

# def partition_numbers(numbers):
#     # this function breaks numbers into a left, pivot, and right
#     left = []
#     pivot = numbers[0]
#     right = []

#     # partition the numbers correctly into left and right arrays
#         # starting loop at second index so that pivot does not get included in left or right sides
#     for num in numbers[1:]:
#         if num <= pivot:
#             left.append(num)
#         else:
#             right.append(num)

#     return left, pivot, right

# def quick_sort_Art(numbers):
#     # base case
#     if len(numbers) <= 1:
#         return numbers

#     left, pivot, right = partition_numbers(numbers)

#     return quick_sort_Art(left) + [pivot] + quick_sort_Art(right)
    

# print(quick_sort_Art([5,9,3,7,2,8,1,6]))
    
