#Assignment 1

runstring = """
def math(a, b):
 sum = float(a) + float(b);
 sub = float(a) - float(b);
 mul = float(a) * float(b);
 div = float(a) / float(b);
 
 print('{0} plus {1} is {2}'.format(a, b, sum))
 print('{0} minus {1} is {2}'.format(a, b, sub))
 print('{0} times {1} is {2}'.format(a, b, mul))
 print('{0} divided by {1} is {2}'.format(a, b, div))

math(100, 10)

"""
exec(runstring)


#Assignment 2
def str_mid(str, word):
    return str[:6] + word + str[6:]

print("Printing the underscores in between the word actioncode: " + str_mid('actioncode', '_'))
 


