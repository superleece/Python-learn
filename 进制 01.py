# -*- coding: cp936 -*-

n = input('How many times do you want to play?:')

i = 0

while i < int(n) :

    r = []

    a = int(input('what is the number to be binary:'))

    b = int(input('what is the number to be base:'))
   
    c = a
  
    while c >= b:

        r.append( c % b)
 
        c = int(c / b)      

    if c<b:

        r.append (c)
    
    print  ('The number is', r[::-1])

    i = i + 1

print ('ngame over')

#待解决问题：Π进制如何处理？
