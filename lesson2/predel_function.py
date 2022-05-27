import math
n=100000

vals = [('log log_2 n' , math.log(math.log(n, 2))),
        ('sqrt log_4 n' ,math.sqrt(math.log(n, 4))),
        ('log_3 n', math.log(n, 3)),
        ('(log_2 n)^2', math.log(n, 2) ** 2),
        ('sqrt n' , math.sqrt(n)),
        ('n / log_5 n'  ,n / math.log(n, 5)),
        ('log (n!)', math.log(math.factorial(n),2)),
        ('3 ^ log_2(n)', 3 ** math.log(n, 2)),
        ('n ^2 ', n ** 2),
        ('7 ^ log_2(n) ',7 ** (math.log(n, 2))),
        ('log_2(n) ^ log_2(n) ',  math.log(n, 2) ** (math.log(n, 2))),
        ('n^ log_2 (n) ', n ** (math.log(n, 2))),
        ('n^ sqrt n ' , n ** (math.sqrt(n))),
        ('2 ** (3 * n)' , 2 ** (3 * n)),
        ('2**n ' , 2**n),
        ('4**n' , 4**n),

        ('n!' , math.factorial(n))
        ]
# champion: print(2 ** (2 ** n))
vals = sorted(vals, key = lambda x : x[1])

print(*[x[0] for x in vals], sep = "\n")

n=100000

print(math.log(math.log(n, 2)))
print(math.sqrt(math.log(n, 4)))
print(math.log(n, 3))
print(math.log(n, 2) ** 2)
print(math.sqrt(n))
print(n / math.log(n, 5))
print(math.log(math.factorial(n),2))
print(3 ** math.log(n, 2))
print(n ** 2)
print(7 ** (math.log(n, 2)))
print(math.log(n, 2) ** (math.log(n, 2)))
print(n ** (math.log(n, 2)))
print(n ** (math.sqrt(n)))
print(2 ** n)
print(4 ** n)
print(2 ** (3 * n))
print(math.factorial(n))