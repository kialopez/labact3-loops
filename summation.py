n = int(4)

sum = 0
formula_str = ""

for i in range(1, n+1):
    sum += i
    formula_str += str(i)
    if i < n:
        formula_str += "+"

print("input:" ,n)
print("formula:" ,formula_str)
print("output:" ,sum)