# This entrypoint file to be used in development. Start by reading README.md
import numpy as np
import mean_var_std
from unittest import main
nums=[1,2,3,4,5,6,7,8,9]
if len(nums)>9:
    print("Not more than 9 values")
else:
    x=np.array(nums)
    matrix=x.reshape(3,3)
    calculations={}
    mean0=np.mean(matrix)
    mean1=np.mean(matrix,axis=0)
    mean2=np.mean(matrix,axis=1)
    var0=np.var(matrix)
    var1=np.var(matrix,axis=0)
    var2=np.var(matrix,axis=1)
    std0=np.std(matrix)
    std1=np.std(matrix,axis=0)
    std2=np.std(matrix,axis=1)
    max0=np.max(matrix)
    max1=np.max(matrix,axis=0)
    max2=np.max(matrix,axis=1)
    min0=np.min(matrix)
    min1=np.min(matrix,axis=0)
    min2=np.min(matrix,axis=1)
    sum0=np.sum(matrix,axis=0)
    sum1=np.sum(matrix,axis=1)
    sum=np.sum(matrix)
    calculations['mean']=mean0, mean1, mean2
    calculations['standard deviation']=std0, std1, std2
    calculations['Maximum']=max0, max1, max2
    calculations['variance']=var0, var1, var2
    calculations['Minimum']=min0, min1, min2
    calculations['Sum']=sum0, sum1,sum
    print(calculations)

# Run unit tests automatically
main(module='test_module', exit=False)