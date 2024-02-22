import re

#text="was"
text=r"[A-Z]+rogram"

paragraph="""
My name was krishna. 
I was a good python programmer.
I loved programming
Program
Drogram
program
dogram
I don't like studying
"""

'''
# re.search() = only shows first occurences and stops there
match=re.search(text, paragraph)
print(match)
'''

matches=re.finditer(text, paragraph)

for match in matches:
    print(match)