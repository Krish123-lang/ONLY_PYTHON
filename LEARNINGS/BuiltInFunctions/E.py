# enumerate() =>Takes a collection (e.g. a tuple) and returns it as an enumerate object
'''
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y)) # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
'''
# *********************************************************************
# eval() => evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
'''
x = 'print(55)'
eval(x) # 55
'''
# *********************************************************************
'''
The exec() function executes the specified Python code.
The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
'''
'''
x = 'name = "John"\nprint(name)'
exec(x) # John
'''
# *********************************************************************
