'''
txt = "My name is Ståle"

x = txt.encode()

print(x) # b'My name is St\xc3\xa5le'
'''
# Syntax: string.encode(encoding=encoding, errors=errors)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

'''
b'My name is St\\xe5le'
b'My name is Stle'
b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
b'My name is St?le'
b'My name is St&#229;le'
'''