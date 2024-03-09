years = int(input("Enter the year: "))

print("Leap Year" if (years % 400 == 0 and years % 100 == 0) else ("Leap year" if (years % 4 == 0 and years % 100 != 0) else "Not Leap year"))


'''
Enter the year: 2016
Leap year

--------------------------------

Enter the year: 2017
Not Leap year
'''