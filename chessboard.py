#https://unstop.com/code/challenge-assessment/250904?moduleId=372
#unstop 100 days challenge - day 1 problem 1

s=input()
a=int(ord(s[0]))
b=int(s[1])
print(f"{"Black" if (a+b)%2==0 else 'White'}")
