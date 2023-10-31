# Zadanie 3.1

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
    # Widać, że kod działa poprawnie

#for i in "axby": if ord(i) < 100: print (i)
    # Powyższa linia kodu jest niepoprawna, "if" powinien zostać przeniesiony do następnej liniki:
for i in "axby": 
    if ord(i) < 100: print (i)
    
for i in "axby": print (ord(i) if ord(i) < 100 else i)
    #Kod działa poprawnie
    
# Zadanie 3.2
# 1) L.sort() sortuje L a nie zwraca posortowaną liste
# 2) Liczba wartości i zmiennych nie zgadza się ze sobą
# 3) Lista X powinna być zdefinowana z użyciem nawiasów
# 4) W kodzie występuje odwołanie do nieistnijącego elementu listy
# 5).append jest metodą listy a nie stringa, którym jest X
# 6) funkcja pow nie dostała argumentów

# Zadanie 3.3
for i in range (31):
    if i%3!=0: print(i)
    
# Zadanie 3.4
while True:
    i = input()
    if str(i)=="stop":
        break

    try: 
        print(float(i), float(i)**3)
    except: 
        print("blad")
        
# Zadanie 3.5
n = 13
s ="|\n"
for i in range(n):
    s = "|...." + s
    s = s + str(i)
    for y in range(5-len(str(i+1))):
        s = s + " "
s = s + str(n)
print(s)
     
# Zadanie 3.6
a = 2
b = 4
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
print(s)

# Zadanie 3.8
sq1 = [1, 3 , 4 , "dwa"]
sq2 = [2, 3, 4, "dwa", "trzy"]
print(list(set(sq1) & set(sq2)))
print(list(set(sq1+sq2)))

# Zadanie 3.9
sq = [[], [1,2], (2,3,4), [5,8]]
for i in range(len(sq)):
    sq[i] = sum(sq[i])
print(sq)

# Zadanie 3.10
dict0 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

dict1 = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])

def RomanToInt(R):
    R = R + " " + " "
    n = 0
    for i in range(len(R)-2):
        R0 = dict0[R[i]]
        if R[i+1]==" ": R1 = 0
        else: R1 = dict0[R[i+1]]
            
        if R[i+2]==" ": R2 = 0
        else: R2 = dict0[R[i+2]]
            
        if R0 > R1: n += R0
        else: 
            if R0 < R1: n += -R0
            
    return n

print(RomanToInt("CMXCV"))
