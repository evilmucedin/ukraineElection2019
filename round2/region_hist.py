#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

bins = []
for i in range(101):
    bins.append([0, 0, 0, 0, 0, 0, 0])

regionname = {}

def createBins():
    poroshenkoBins = [0.0]*101
    zelenskiyBins = [0.0]*101
    return [poroshenkoBins, zelenskiyBins]

regions = {}
for i in range(-1, 100):
    regions[i] = createBins()

with open("data.csv", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        total = int(row[1])
        votes = int(row[6])
        poroshenko = int(row[11])
        zelenskiy = int(row[10])
        region = int(row[-2])
        regionname[region] = row[-1]
        assert poroshenko <= votes
        assert zelenskiy <= votes
        aregion = regions[region]
        # print(total, votes, poroshenko, timoshenko, zelenskiy)
        if votes:
            poroshenkoRatio = float(poroshenko)/float(votes)
            zelenskiyRatio = float(zelenskiy)/float(votes)
            poroshenkoBin = int(100.0 * poroshenkoRatio)
            aregion[0][poroshenkoBin] += poroshenko
            zelenskiyBin = int(100.0 * zelenskiyRatio)
            aregion[1][zelenskiyBin] += zelenskiy

bins = []
for i in range(101):
    bins.append(i)

for region in regions.keys():
    if region not in regionname:
        continue
    plt.clf()
    aregion = regions[region]
    plt.scatter(bins, aregion[0], color='red', s=7, label="Poroshenko")
    plt.scatter(bins, aregion[1], color='green', s=7, label="Zelenskiy")
    plt.legend()
    plt.suptitle(regionname[region])
    plt.savefig("ptz.%s.png" % regionname[region], dpi=300)
