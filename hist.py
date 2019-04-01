#!/usr/bin/env python3

import csv

bins = []
for i in range(101):
    bins.append([0, 0])

with open("data.csv", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        total = int(row[1])
        votes = int(row[6])
        poroshenko = int(row[39])
        print(total, votes, poroshenko)
        if votes:
            turnover = float(votes)/total
            poroshenkoRatio = float(poroshenko)/float(votes)
            bn = int(turnover * 100.)
            bins[bn][0] += 1
            bins[bn][1] += poroshenkoRatio

for i in range(101):
    if bins[i][0]:
        print(i, bins[i][1]/bins[i][0])
