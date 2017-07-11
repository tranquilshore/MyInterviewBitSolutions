A = [2,2]

ans = list()
for i in range(len(A)):
    if A[abs(A[i]) - 1] > 0:
        A[abs(A[i]) - 1] = - A[abs(A[i]) - 1]
    else:
        ans.append(abs(A[i]))

for i in range(len(A)):
    if A[i] > 0:
        ans.append(i+1)
print ans
    
