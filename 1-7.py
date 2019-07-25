n1=int(input())
s1=0
for v1 in range(0,n1):
  if(pow(2,v1)>n1):
    break
  s1=n1-pow(2,v1)
print(s1)
