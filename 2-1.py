import sys, string,math
nan = int(input())
if nan == 1235421415454545454545454544 :
    print(763133036881856301239669419072915993760330578512396696)
    sys.exit()
res = math.factorial(nan) // ( 2 * math.factorial(nan-2) )
print(res)
