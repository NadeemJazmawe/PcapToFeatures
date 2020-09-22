import csv

'''
to write new file we put "w" in open function.
to write over the file we put "a" in open function.
'''
with open("MyCSV.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Col1', 'Col2', 'Col3'])
    writer.writerow(['one', 'two', 'three'])
