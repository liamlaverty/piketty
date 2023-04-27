# prints fibonacci sequence
a, b = 0, 1
itterator = 0
while itterator < 1000: 
    print ('{}\n\n'.format(a))
    a, b = b, a + b

print('reached the end of the loop')