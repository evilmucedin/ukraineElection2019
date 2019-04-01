#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

bins = []
for i in range(101):
    bins.append([0, 0, 0, 0, 0, 0, 0])

poroshenkoBins = [0.0]*101
timoshenkoBins = [0.0]*101
zelenskiyBins = [0.0]*101

fPoroshenko = open("poroshenko.tsv", "w")
fTimoshenko = open("timoshenko.tsv", "w")
fZelenskiy = open("zelenskiy.tsv", "w")

aturnover = []
aporoshenko = []
atimoshenko = []
azelenskiy = []
with open("data.csv", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        total = int(row[1])
        votes = int(row[6])
        poroshenko = int(row[39])
        timoshenko = int(row[45])
        zelenskiy = int(row[23])
        assert poroshenko <= votes
        assert timoshenko <= votes
        assert zelenskiy <= votes
        # print(total, votes, poroshenko, timoshenko, zelenskiy)
        if votes:
            turnover = float(votes)/total
            aturnover.append(turnover)
            aporoshenko.append(poroshenko)
            atimoshenko.append(timoshenko)
            azelenskiy.append(zelenskiy)
            print(turnover, poroshenko, file=fPoroshenko)
            print(turnover, timoshenko, file=fTimoshenko)
            print(turnover, zelenskiy, file=fZelenskiy)
            poroshenkoRatio = float(poroshenko)/float(votes)
            timoshenkoRatio = float(timoshenko)/float(votes)
            zelenskiyRatio = float(zelenskiy)/float(votes)
            bn = int(turnover * 100.)
            bins[bn][0] += 1
            bins[bn][1] += poroshenko
            bins[bn][2] += timoshenko
            bins[bn][3] += zelenskiy
            bins[bn][4] += poroshenkoRatio
            bins[bn][5] += timoshenkoRatio
            poroshenkoBin = int(100.0 * poroshenkoRatio)
            poroshenkoBins[poroshenkoBin] += poroshenko
            timoshenkoBin = int(100.0 * timoshenkoRatio)
            timoshenkoBins[timoshenkoBin] += timoshenko
            zelenskiyBin = int(100.0 * zelenskiyRatio)
            zelenskiyBins[zelenskiyBin] += zelenskiy

plt.scatter(aturnover, aporoshenko, color='red', s=7, label="Poroshenko")
plt.scatter(aturnover, atimoshenko, color='yellow', s=7, label="Timoshenko")
plt.scatter(aturnover, azelenskiy, color='green', s=7, label="Zelenskiy")
plt.legend()
plt.show()
plt.savefig("ptz.png", dpi=300)

with open("pt.tsv", "w") as f:
    for i in range(101):
        if bins[i][0]:
            print(i, bins[i][0]*100, bins[i][1], bins[i][2], bins[i][3], bins[i][4]/bins[i][0], bins[i][5]/bins[i][0], file=f)

with open("p.tsv", "w") as f:
    for i in range(101):
        print(i, poroshenkoBins[i], timoshenkoBins[i], zelenskiyBins[i], file=f)
