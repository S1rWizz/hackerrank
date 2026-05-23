# https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/
# reversing a list

a=input()
l=list(map(int,a[1:-1].split(',')))

print(l[::-1])