#!/usr/bin/env python3

import csv

bins = []
for i in range(101):
    bins.append([0, 0, 0, 0, 0])

poroshenkoBins = [0.0]*101
timoshenkoBins = [0.0]*101

with open("data.csv", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        total = int(row[1])
        votes = int(row[6])
        poroshenko = int(row[39])
        timoshenko = int(row[45])
        assert poroshenko <= votes
        assert timoshenko <= votes
        # print(total, votes, poroshenko, timoshenko)
        if votes:
            turnover = float(votes)/total
            poroshenkoRatio = float(poroshenko)/float(votes)
            timoshenkoRatio = float(timoshenko)/float(votes)
            bn = int(turnover * 100.)
            bins[bn][0] += 1
            bins[bn][1] += poroshenko
            bins[bn][2] += timoshenko
            bins[bn][3] += poroshenkoRatio
            bins[bn][4] += timoshenkoRatio
            poroshenkoBin = int(100.0 * poroshenkoRatio)
            poroshenkoBins[poroshenkoBin] += poroshenko
            timoshenkoBin = int(100.0 * timoshenkoRatio)
            timoshenkoBins[timoshenkoBin] += timoshenko

with open("pt.tsv", "w") as f:
    for i in range(101):
        if bins[i][0]:
            print(i, bins[i][1], bins[i][2], bins[i][3]/bins[i][0], bins[i][4]/bins[i][0], file=f)

with open("p.tsv", "w") as f:
    for i in range(101):
        print(i, poroshenkoBins[i], timoshenkoBins[i], file=f)
