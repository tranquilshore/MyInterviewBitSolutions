import sys

A = [1,3,-1]
def maxArr( A):
    a_size = len(A)
    max1=max2=max3=max4=ans = -sys.maxint - 1
    for i in range(a_size):
        max1 = max(max1, A[i]+i)
        max2 = max(max2, A[i]-i)
        max3 = max(max3, -A[i]+i)
        max4 = max(max4, -A[i]-i)
    
    for j in range(a_size):
        ans = max(ans, max1-A[j]-j)
        ans = max(ans, max2-A[j]+j)
        ans = max(ans, max3+A[j]-j)
        ans = max(ans, max4+A[j]+j)
    return ans

print maxArr(A)