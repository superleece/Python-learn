def isprime0(n):
    
    j = 0
    
    i = 1
    
    while i <= n:
        
        if n % i ==0:
            
            j += 1
            
        i += 1

    if j == 2:

        return True

    return False


'''x = isprime0(15)

print(x)

x = isprime0(7)

print(x)'''

########################################

def isprime1(n):
    
    r = []
    
    i = 1
    
    while i <= n:
        
        if n % i ==0:
            
            r.append(i)
            
        i += 1

    if len(r) == 2:

        return True, r

    return False, r

def primefactor(lis):

    c = []

    i = 1

    for i in range(len(lis)-1):

        if isprime0(lis[i]) == True:

            c.append(lis[i])

    return c

def prime(n):

    x, y = isprime1(n)

    z = primefactor(y)

    return x, z



a, b = prime(100)

print(a, b)

a, b = prime(91)

print(a, b)

            
'''x, y = isprime1(15)

print(x, y)

z = primefactor(y)

print(z)

x, y = isprime1(7)

z = primefactor(y)

print(x, y)
print(z)'''






    


