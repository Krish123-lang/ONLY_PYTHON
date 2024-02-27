txt = "Hello, welcome to my world."

# x = txt.endswith(".")

# print(x) # True

# Syntax: string.endswith(value, start, end)


# x = txt.endswith("my world.")

# print(x) # True

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x) # False
