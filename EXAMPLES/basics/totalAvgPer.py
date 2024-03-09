maths = float(input("Enter marks in maths: "))
physics = float(input("Enter marks in physics: "))
chemistry = float(input("Enter marks in chemistry: "))
nepali = float(input("Enter marks in nepali: "))
workshop = float(input("Enter marks in workshop: "))

total = maths+physics+chemistry+nepali+workshop
avg = total/5
per = (total/500)*100

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Percentage: {per} %")

'''
Enter marks in maths: 67
Enter marks in physics: 4
Enter marks in chemistry: 77
Enter marks in nepali: 67
Enter marks in workshop: 56
Total: 271.0
Average: 54.2
Percentage: 54.2 %
'''