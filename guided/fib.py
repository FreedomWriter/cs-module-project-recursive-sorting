def fib(n):
    # base case
    if n == 1 or n == 2:
        return 1
    
    #recursive case
    else:
        return fib(n-1) + fib(n-2)

print(fib(20))

def fib2(n):
    # base case
    if n == 1 :
        return 1
    if n == 0:
        return 0
    #recursive case
   
    result = fib2(n-1) + fib2(n-2)
    return result

print(fib2(20))

def iterative_fib(n):
    if n == 1 or n== 2:
        return 1
    else:
        prevprev = 1
        prev = 1
        cur = prev + prevprev
        for i in range(2, n):
            temp = cur
            cur = prev + prevprev
            prevprev = prev
            prev = temp
    return cur