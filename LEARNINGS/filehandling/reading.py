''' with open('testfile.txt', 'w') as f:
    f.write("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")
    f.close() '''


# with open('testfile.txt', 'r') as r:
# print(r.readline())  # prints only the first line from the file
# print(r.readlines())  # prints the contents of the file in a list format
# print(r.read())  # prints the contents of the file
# r.close()

# with open('testfile.txt') as f:
# loop through all the list of strings in lines list
# using strip() function to remove whitespaces
# [print(lines.strip()) for lines in f.readlines()]

with open('testfile.txt', encoding='utf-8') as f:
    for lines in f:
        print(lines.strip())
