n,m=map(int,input().split())
v_half=n//2
mid=(m-7)//2

#upper half
k=1
j=(m-(3*k))//2
for i in range(v_half):
    print(f"{'-'*j}{'.|.'*k}{'-'*j}")
    k+=2
    j=(m-(3*k))//2

#middle
print(f"{'-'*mid}WELCOME{'-'*mid}")

#lower half (different var as using k,j causing probs)
x=k-2
y=(m-(x*3))//2

for j in range (v_half,0,-1):
    print(f"{'-'*y}{'.|.'*x}{'-'*y}")
    x-=2
    y=(m-(x*3))//2