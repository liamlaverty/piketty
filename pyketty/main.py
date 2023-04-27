# to launch, open cmd and run: 
#   cd .\pyketty\
#   py .\main.py 

x = 2
if x == 1:
    print('x is equal to 1')
else:
    print('x is not equal to 1')


# commenting
spam = 1    # this is a comment
            # this is another comment
text = "this is not a comment"            


# calculators
answer = 0

answer = 2+2
print('addition: {}'.format(answer))
print("----====----")


answer = 50-5*6
print('multi operator: {}'.format(answer))
print("----====----")


answer = 17/3
print('division with flop: {}'.format(answer))
print("----====----")


answer = 17//3
print('division with floor: {}'.format(answer))
print("----====----")


answer = 17 % 3
print('remainders: {}'.format(answer))
print("----====----")


answer = 17 ** 2
print('squared: {}'.format(answer))
print("----====----")

answer = 17 ** 14
print('A to the power of B: {}'.format(answer))
print("----====----")

def power(a, b):
    return a ** b

answer = power(17, 14)
print('A to the power of B in a function: {}'.format(answer))
print("----====----")


stringLiteral = """this is a 
multiline string 
    with tabs \n
    and an extra newline using \\n"""
print (stringLiteral)
print("----====----")


print("multipart word joined together")
print("py" "thon")
print("----====----")

print("multipart word with multiplication")
print(3 * "test" + "sample")
print("----====----")


my_prefix = 'py'
print (my_prefix + 'thon')
print("----====----")

my_word = 'python'
print('char index from the start of a string')
print (my_word[0] + my_word[1] + 'thon')
print("----====----")


print('char index from the end of string')
print (my_word[-1] + my_word[-4] + 'thon')
print("----====----")

print('char index and the number 0 (both 0 and -0 are the same index)')
print (my_word[0] + my_word[-0])
print("----====----")


print('char index, characters between')
print (my_word[0:3])
print("----====----")


print('char index, from index to end')
print (my_word[:4])
print("----====----")

print('char index, from index to end using opposite syntax')
print (my_word[4:])
print("----====----")


print('out of range exception')
try:
    print (my_word[20])
except IndexError: 
    print('encountered expected IndexError')
print("----====----")

print('char slicing doens\'t throw exception')
print (my_word[6:20])
print("----====----")