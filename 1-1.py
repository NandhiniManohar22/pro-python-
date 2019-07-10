def longest(n1,n2):
  if n1 in n2:
      return n1
  else:
     return longest(k[0:len[k]-1],n2)
num=int(input())
char=[]
for _ in range(0,num):
   char.append(input())
che.sort()
print(longest(char[0],char[num-1]))
