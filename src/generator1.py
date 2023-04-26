import numpy as np
def generator1(x,a=16807,q=127773,r=2836):
    # x= 127973
    m=a*q+r
    h=(np.uint(x/q)) 
    # print("h: ",h)
    l= np.uint(x%q)
    # print("l: ",l)
    test = a * l - r * h
    # print("test: ",test)
    xx=(a*(x - (q*h))) - (r*h)
    # print("xx: ",xx)
    if (xx<0):
        xx=xx+2147483647
    result=(xx/2147483647)
    # print(result)
    return xx,m,result

print(generator1(1))
results,m,random=generator1(1)
print (m)
results=1
print(float(results/m))
for i in range(30):
    results,m,random=generator1(results)
    print(results,random)
