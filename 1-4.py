kk1,l1=map(str,input().split())
east=0
if len(kk1)>len(l1):
  kk1,l1=l1,kk1
tt1=0
while tt1<len(kk1):
  east+=(ord(l1[tt1])-ord(kt1[tt1]))
  tt1+=1
for tt1 in range(tt1,len(l1)):
  east+=ord(l1[tt1])-ord('a')+1
print(east)
