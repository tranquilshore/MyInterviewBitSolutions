A = 4
mat = [[0 for j in range(A)] for i in range(A)]
if A == 0:
    print mat

i = 1
x = 0
y = 0
mat[0][0] = i

i += 1
while i <= A*A:
    while y+1 < A and mat[x][y+1] == 0:#goin right
        y += 1
        mat[x][y] = i
        i += 1
    while x+1 < A and mat[x+1][y] == 0:#goin down
        x += 1
        mat[x][y] = i
        i += 1
    while y-1 >= 0 and mat[x][y-1] == 0:#goin left
        y -= 1
        mat[x][y] = i
        i += 1
    while x-1 >= 0 and mat[x-1][y] == 0:
        x -= 1
        mat[x][y] = i
        i += 1
print mat
    
    