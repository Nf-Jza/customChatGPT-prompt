import csv

# Read and display CSV data
file_name = 'nvimCgptprompt.csv'  # Replace with your CSV file name

with open(file_name, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
