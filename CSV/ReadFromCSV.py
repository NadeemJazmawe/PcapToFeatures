import csv

def readCSV(FileName):
    with open(FileName) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def readCSVtoArray(FileName):
    with open(FileName) as file:
        arr = list(csv.reader(file))

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j], ",", end="")
        print()

    return arr

readCSVtoArray("Student.csv")