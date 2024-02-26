# Args are treated as tuple, so we can access the values using indexes

'''
def greet(name):
    return f"Hello, {name}"

g=greet("Krishna")
print(g)
'''
# *******************************************************************
# ARGS

'''
def hello(*argv):
    for arg in argv:
        print(arg)


hello("Hello", "this", "is", "Krishna")
'''

'''
Hello
this
is
Krishna
'''
# *******************************************************************

'''
def hello(arg1, *argv):
    print(f"first argument: {arg1}\n")

    for arg in argv:
        print(f"Argv* : {arg}")


hello("This", "is", "krishna", "mandal")
'''

'''
first argument: This

Argv* : is
Argv* : krishna
Argv* : mandal
'''
# ******************************************************************

