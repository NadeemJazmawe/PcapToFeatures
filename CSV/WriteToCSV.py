import csv

with open("MyCSV.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Col1', 'Col2', 'Col3'])
    writer.writerow(['one', 'two', 'three'])
