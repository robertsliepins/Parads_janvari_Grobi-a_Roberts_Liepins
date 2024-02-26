import csv
file_name = "uzd2.csv"

with open(file_name, "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        if len(row) >= 3:
            print(row[2])