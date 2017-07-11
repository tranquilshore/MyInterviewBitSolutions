import sys
s = "0011101"

'''
For maximum zeros:
The idea is to consider every 0 as -1 and every 1 as 1.

For maximum Ones:
The idea is to consider every 1 as -1 and every 0 as 1.
'''


#subarray of maximum 1's after a flip
#ans = 1,2
ns = list()
for i in range(len(s)):
    if s[i] == "1":
        ns.append("-1")
    else:
        ns.append("1")
        
ns = [int(x) for x in ns]

maxSoFar = -sys.maxint - 1
maxEndHere = 0

start = 0
end = 0

s = 0

for i in range(len(ns)):
    maxEndHere += ns[i]
    
    if maxSoFar < maxEndHere:
        maxSoFar = maxEndHere
        start = s
        end = i
    if maxEndHere < 0:
        maxEndHere = 0
        s = i+1
res = list()
res.append(start)
res.append(end)

print res



        
