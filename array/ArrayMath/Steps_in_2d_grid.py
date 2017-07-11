import math
def coverPoints(X, Y):
    val = 0
    for i in range(len(X)-1):
        val += max(abs(X[i] - X[i+1]) , abs(Y[i] - Y[i+1]))
    print val
                   
                   
x = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
y = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
coverPoints(x,y)