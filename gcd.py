print("this progamme is to get the Great Common Dividor for 2 number")

a = int(input('please input the first number:\n'))

b = int(input('please input the second number:\n'))

s = 0

i = 1

gcd = 1

if a < b:
    
    s = a
    
elif b <= a:#此处不需要用elif,直接用else即可
    
    s = b
    
while i <= s:
    
    if a%i == 0 and b%i == 0:
        
        gcd = i
        
    i += 1

print ('the Great Common Dividor of {0} and {1} is {2}'.format(a, b, gcd))
