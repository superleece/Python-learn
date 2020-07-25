r = []
h = []
a = int(input('please input the number:'))
print (a)
s = a
print (s)
i = 1

g = 0

while i <= s:
    
    if a%i == 0 :
        
        g = i
        k = 1
        while k<=g:
            if g%k==0:
                h.append(k)
                print (h)
            k+=1
                print(k,g)
                
    i += 1
    print(i)

print (r)


