# Zadanie 2.10
line = """test wielowierszowego
wyrażenia 123 GvR"""
print("2.10: ", len([x for x in line.split()]))

# Zadanie 2.11
print("2.11: ", '_'.join(x for x in [*"word"]))

# Zadanie 2.12
print("2.12a: ", ' '.join(x[0] for x in line.split()))
print("2.12b: ", ' '.join(x[len(x)-1] for x in line.split()))

# Zadanie 2.13
print("2.13: ", max(line.split(), key=len), len(max(line.split(), key=len)))

# Zadanie 2.15
L = [1, 6, 7, 8, 0, 2]
print("2.15: ", ''.join(str(x) for x in L))

# Zadanie 2.16
s = []
for x in line.split(): 
    if x=="GvR": s.append("Guido van Rossum") 
    else: s.append(x)
print("2.16: ", ' '.join(x for x in s))

# Zadanie 2.17 
print("2.17a: ", *sorted(line.split(), key=str.lower)) # zakładjąc, że nie zwracamy uwagi na duże litery
print("2.17b: ", *sorted(line.split(), key=len))

# Zadanie 2.18
z = 123487982000483473800000874938000
print("2.18: ", str(z).count('0'))

# Zadanie 2.19
L = [177, 23, 444, 134, 10, 333, 12]
print("2.19: ", ''.join(str(x).zfill(3) for x in L))