from book import Book
import time
import csv
​
def insertion_sort(books):
    # loop through len-1 elements
    for i in range(1, len(books)):
        temp = books[i]
        j = i
        while j > 0 and temp.genre < books[j - 1].genre:
            # shift left until correct genre found
            books[j] = books[j - 1]
            j -= 1
        # insert at correct position
        books[j] = temp
​
    return books
​
# Version A: Conventional, recursive Quick Sort
def quick_sort_A( books, low, high ):
     #To-DO:
    # BASE - we are trying to sort a single element
    if len(books) <= 1:
        return books
    # RECURSIVE - 
    #choose a pivot
    pivot = books[0].author
    LHS = []
    RHS = []
    for i in range(1, len(books)):

        if books[i].author < pivot:
            LHS.append(books[i])
        elif books[i].author >= pivot:
            RHS.append(books[i])
    # elif el > pivot, move to RHS

    return quick_sor_a(LHS) + [pivot] + quick_sor_a(RHS)
​
​
# Version B:
# NOT done in place because for large inputs, we
# exceed Python's maximum recursion depth with 
# in-place Quick Sort
def quick_sort_B( books ):
    # STRETCH: implement Quick Sort for larger datasets
​
    return books
​
​
def book_sort(books):
    # STRETCH: combine Insertion & Quick Sort for
    # an improved sorting algorithm
    
    return books
​
# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('book_data.csv') as csvfile:
    my_books_long = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books_long.append(Book(book['title'], book['author'], book['genre']))
    my_books_medium = my_books_long[0:997]
    my_books_short = my_books_long[0:10]
​
print("***********~Test with 10 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_short)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")
​
start = time.time()
sorted_books = quick_sort_A(my_books_short, 0, len(my_books_short))
end = time.time()
print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")
​
​
print("\n***********~Test with ~1,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_medium)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")
​
start = time.time()
sorted_books = quick_sort_A(my_books_medium, 0, len(my_books_medium))
end = time.time()
print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")
​
​
print("\n**********~Test with +2,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_long)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")
​
# start = time.time()
# sorted_books = quick_sort_B(my_books_long)
# end = time.time()
# print("Quick Sort (B) took:  " + str((end - start)*1000) + " milliseconds")
​
# start = time.time()
# sorted_books = book_sort(my_books_long)
# end = time.time()
# print("Book Sort took:       " + str((end - start)*1000) + " milliseconds\n")

import time
# [5,9,3,7,2,8,1,6]
# Chose a pivot
#     take first number in list - 5
# Move all elements smaller than pivot, to the left of the pivot
# Move all elements larger than pivot, to the right of pivot
# [3,2,1][5][9,7,8,9]
# Repeat the process on the two new arrays (left and right) - the pivot is where it's supposed to be
# arrays of one are the base case - they are sorted
#     each recursive call get the arrays they return combined and then returned

def partition_numbers(numbers):
    # this function breaks numbers into a left, pivot, and right
    left = []
    pivot = numbers[0]
    right = []

    # partition the numbers correctly into left and right arrays
        # starting loop at second index so that pivot does not get included in left or right sides
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right

def quick_sort_Art(numbers):
    # base case
    if len(numbers) <= 1:
        return numbers

    left, pivot, right = partition_numbers(numbers)

    return quick_sort_Art(left) + [pivot] + quick_sort_Art(right)
    

print(quick_sort_Art([5,9,3,7,2,8,1,6]))