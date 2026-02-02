import csv

total = 0

with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["precio"])
        quantity = int(row["cantidad"])
        total += price * quantity

print("Total sales:", total)