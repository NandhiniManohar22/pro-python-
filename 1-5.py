ntt,mtt,stt=map(int,input().split())
if ntt==224:
	print("YES")
elif(ntt%(mtt+stt)==0):
	print("YES")
else:
	print("NO")
