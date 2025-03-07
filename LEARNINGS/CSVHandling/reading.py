import csv
'''
f = open('country.csv', encoding='UTF8')
csv_reader = csv.reader(f)
for lines in csv_reader:
    print(lines)
f.close()
'''

# ====================================
# with open('country.csv', 'r', encoding='UTF-8') as f:
#     csv_reader = csv.reader(f)
# for lines in csv_reader:
#     # print(lines[0]) # country's names
#     # print(lines[1]) # country's area
#     print(lines)

# for line_no, line in enumerate(csv_reader, 1):
#     if line_no == 1:
#         print('Header:')
#         print(line)  # header
#         print('Data:')
#     else:
#         print(line)  # data

# --------------------------------------------------

with open('country.csv', 'r', encoding='UTF8') as f:
    csv_reader = csv.DictReader(f)
    next(csv_reader)
    for lines in csv_reader:
        print(f"The area of {lines['name']} is: {lines['area']} km2")
