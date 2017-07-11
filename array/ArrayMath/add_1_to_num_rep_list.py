a = [ 0, 3, 7, 6, 4, 0, 5, 5, 5 ]


def addOne(a):
    a.reverse()
    i = 0
    b = list()
    carry = 1
    while i < len(a):
        #addition
        sum_ = carry + a[i]
        
        #updating carry
        if sum_ >= 10:
            carry = 1
        else:
            carry = 0
        
        #updating sum_ if >= 10
        sum_ = sum_ % 10
        
        b.append(sum_)
        i += 1
    
    #if some carry left at the end append it to the result
    if carry > 0:
        b.append(carry)
    b.reverse()
    
    #code to remove trailing zeros
    count = 0
    for i in range(len(b)):
        if b[i] == 0:
            count += 1
        else:
            break

    for i in range(count):
        del b[0]
    
    return b

print addOne(a)