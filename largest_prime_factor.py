from sympy import isprime,divisors
n=600851475143
l=divisors(n)
for i in range(len(l)-1,0,-1):
    if isprime(l[i])==True:
        print(l[i])
        break