def sum_of_digits(n):
    "Sum of digits"
    if n == 0:
        return 0
    else:
        # return n % 10 + sum_of_digits(n//10)
        return n % 10 + sum_of_digits(n//10)


# print(sum_of_digits(123))
# ==================================================

def reverse_digits(n):
    "Reverse a digit"
    convert_to_string = str(n)
    revNum = convert_to_string[::-1]
    reversed_number = int(revNum)
    return reversed_number


# print(reverse_digits(12345))
# ==================================================

def prime_number(n):
    "Prime number Testing"
    if n <= 1:
        return "Not Prime"
    else:
        for i in range(2, n):
            if n % i == 0:
                return "Not Prime Number"
        else:
            return "Prime Number"


# print(prime_number(11))
# ==================================================

