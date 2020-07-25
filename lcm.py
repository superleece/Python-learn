a = int(input('please input the first number:'))

b = int(input('please input the second number:'))

s = 0

i = a*b

lcm= 1
if a > b:
    
    s = a
    
elif b >= a:
    
    s = b
    


while i >= s:    

    
    if i%a == 0 and i%b == 0:
        
        lcm = i
        
    i -= 1


print (lcm)






