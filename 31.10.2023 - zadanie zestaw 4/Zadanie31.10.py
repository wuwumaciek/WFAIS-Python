from math import floor
# Zadanie 4.2
def miarka(n):
    s ="|\n"
    for i in range(n):
        s = "|...." + s
        s = s + str(i)
        for y in range(5-len(str(i+1))):
            s = s + " "
    s = s + str(n)
    return s

    # print(miarka(13))
    
def prostokat(a, b):
    s = "" 
    for i in range(a):
        for y in range(b):
            s = s + "+---"
        s = s + "+\n"
        for y in range(b):
            s = s + "|   "
        s = s + "|\n"
    for y in range(b):
        s = s + "+---"
    s = s + "+"
    return s

    # print(prostokat(2, 4))
    
# Zadanie 4.3
def factorial(n):
    s = 1
    for i in range(n):
        s = s*(i+1)
    return s

    # print(factorial(4))
    
# Zadanie 4. 4
def  fibonacci(n):
    s0 = 0
    s1 = 1
    for i in range(n):
        temp = s0 + s1
        s0 = s1
        s1 = temp
    return s0
    # print(fibonacci(6))
    
# Zadanie 4.5
def Lswap(L, a, b):
    L[a], L[b] = L[b], L[a]
    return L

# Iteracyjnie 
def Iodwracanie(L, left, right):
    for i in range(floor((right-left)/2)+1):
        L = Lswap(L, left+i,right-i)
    return L

    # print(Iodwracanie([1,2,3,4,5,6,7,8,9,10],2,8))
    
# REkurencyjnie
def Rodwracanie(L, left, right):
    L = Lswap(L, left,right)
    if left+1>=right-1:
        return L
    else:
        return Rodwracanie(L,left+1,right-1)

    # print(Rodwracanie([1,2,3,4,5,6,7,8,9,10],2,9))
    
# Zadanie 4.6
def  sum_seq(s):
    sum = 0
    for i in s:
        if isinstance(i, (list, tuple)):
            sum += sum_seq(i)
        else:
            sum += i
    return sum

    # print(sum_seq([1,2,3,[3,2],[1,[2,0],1,0],0]))        
        
# Zadanie 4.7
def flatten(s):
    R = []
    for i in s:
        if isinstance(i, (list, tuple)):
            for y in flatten(i):
                R.append(y)                
        else:
            R.append(i)            
    return R

    # print(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]))