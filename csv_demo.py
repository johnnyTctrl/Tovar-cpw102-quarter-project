import csv

with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Category", "Amount"])
    writer.writerow(["Food", "25.00"])
    writer.writerow(["Gas", "40.00"])
    writer.writerow(["Bills", "100.00"])

print("Expenses saves successfully!")

    