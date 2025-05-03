import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])
    writer.writerow(['David', 28, 'Houston'])

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('data.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row['Name'], row['Age'], row['City'])