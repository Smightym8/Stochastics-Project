import csv

data_file = "../data/penguins.csv"

datasets = []

with open(data_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in reader:
        datasets.append(line)

for dataset in datasets:
    print(dataset)