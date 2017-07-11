A = [1,2,3,-5,2,3,6]
A = [0,0,-1,0]

maxsum = 0
newsum = 0

maxarray = list()
newarray = list()

for i in A:
    if i >= 0:
        newsum += i
        newarray.append(i)
    else:
        newsum = 0
        newarray = list()
    
    if maxsum < newsum or (maxsum == newsum and len(newarray) > len(maxarray)):
        maxsum = newsum
        maxarray = newarray

print maxarray