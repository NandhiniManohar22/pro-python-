n,m=input().split()
nan=abs(len(m)-len(n))
for g in range (len(n)):
  if(len(m)==1 and m[g] in n):
    break
  if(n[g]!=m[g]):
    nan=nan+1
print(nan)    
  
