A = 3

if A == 0:
    print "" #don't move forwared

a=[]
a.append([])
a[0].append(1)
for i in range(1,A):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(A!=0):
        a[i].append(1)
        
print a