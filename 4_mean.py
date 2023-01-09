num1 = [20,65,34,45,23,89,100,43,22,89]
n = len(num1)
print("\n Data to find mean median , mode & sd",num1)
#mean
getsum=sum(num1)
mean=getsum/n
print("Mean is "+str(mean))

#calculating median
num1.sort()
if n%2==0:
    median1=num1[n//2]
    median2=num1[n//2-1]
    median=(median1+median2)/2
else:
    median = num1[n//2]
print("median is "+str(median))

#calculating mode
from collections import Counter
data = Counter(num1)
getmode=dict(data)
mode=[k for k,v in getmode.items()if v==max(list(data.values()))]
if len(mode)==n:
    getmode="no Mode Found"
else:
    getmode="Mode is "+"".join(map(str,mode))
print(getmode)
#finding standard deviation
import numpy as np
print("standard deviation is ",np.std(num1))