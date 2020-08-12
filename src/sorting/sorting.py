# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# print(merge([1,2,3], ['a', 'b', 'c']))
# def merge_helper(a, b):
#     sorted = []
#     ai = 0
#     bi = 0
#     count = len(a) + len(b)
#     while len(sorted) < count:
#         if ai >= len(a):
#             sorted.append(b[bi])
#             bi += 1
#         elif bi >= len(b):
#             sorted.append(a[ai])
#             ai += 1
#         elif a[ai] < b[bi]:
#             sorted.append(a[ai])
#             ai += 1
#         elif a[ai] >= b[bi]:
#             sorted.append(b[bi])
#             bi += 1
#     print(f"count - {count}")
#     print(f"ai - {ai}")
#     print(f"bi - {bi}")
#     print(sorted)
#     return sorted
# # TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):

#     if len(arr) == 0:
#         return None

#     # base case
#     if len(arr) == 1:
#         return arr
    
#     #recursive
#     else:
#         # divide 'arr' into a LHS and a RHS
#         #### find the middle and define LHS, RHS
        # middle = len(arr)  //2
        # LHS= arr[:middle]
        # RHS = arr[middle:]
#         # print(LHS)
#         # print(RHS)
#         merge_sort(LHS)
#         merge_sort(RHS)
#         arr = merge_helper(LHS, RHS)


#         return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        LHS = arr[:mid]
        RHS = arr[mid:]

        # Recursive call on each half
        merge_sort(LHS)
        merge_sort(RHS)

        # Two iterators for traversing the two halves
        right_i = 0
        left_i = 0
        
        # Iterator for the main list
        main_i = 0
        
        while right_i < len(LHS) and left_i < len(RHS):
            if LHS[right_i] < RHS[left_i]:
              # The value from the LHS half has been used
              arr[main_i] = LHS[right_i]
              # Move the iterator forward
              right_i += 1
            else:
                arr[main_i] = RHS[left_i]
                left_i += 1
            # Move to the next slot
            main_i += 1

        # For all the remaining values
        while right_i < len(LHS):
            arr[main_i] = LHS[right_i]
            right_i += 1
            main_i += 1

        while left_i < len(RHS):
            arr[main_i]=RHS[left_i]
            left_i += 1
            main_i += 1
    return arr

my_list = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(my_list))
# print(my_list)

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


    
