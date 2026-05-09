n=int(input())
l=list(map(int,input().split()))
l1=get_power_set(l)
'''while len(l)>1:
  for i in range(0,len(l)):
    for j in range(1,len(l)):
      l1.append([l[i],l[j]])
  break
else:
  print(0)'''
new_l=[]
for i in range(len(l1)):
  if l1[i] not in new_l:
    new_l.append(l1[i])
print(new_l)

