import csv

header = ['name', 'age', 'address']
data = ['krishna', 24, 'katahari']

with open('persons.csv', 'w', encoding='UTF8', newline='') as f:
    person_writer = csv.writer(f)
    person_writer.writerow(header)
    person_writer.writerow(data)
