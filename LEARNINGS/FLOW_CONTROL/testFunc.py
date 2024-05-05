'''
def loan_emi(amount, rate, months=12, down_payment=0):
    #Calculate the monthly installment for loan #
    principal = amount-down_payment
    try:
        factor = rate/(1-1/(1+rate)**months)
    except ZeroDivisionError:
        factor = 1/months
    return principal*factor


l = loan_emi(1200, 10, down_payment=100)
print(l) # 11000.000000003505
'''


def evenListFunc(numberList):
    evenList = []
    for i in numberList:
        if i % 2 == 0:
            evenList.append(i)

    return evenList


evenNum = evenListFunc([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 4])
print(evenNum) # [2, 4, 6, 8, 4]
