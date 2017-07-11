a = [[1,2,3],[4,5,6],[7,8,9]]

n = len(a)
if n == 0:
    print "nothing"
diagonal = list()
result = list()
for d in range(2*(n-1) + 1):
    for i in range(d+1):
        j = d - i
        if i >= n or j >= n:
            continue
        diagonal.append(a[i][j])
    result.append(diagonal)
    diagonal = list()
print result