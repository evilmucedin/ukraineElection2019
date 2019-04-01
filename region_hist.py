#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

bins = []
for i in range(101):
    bins.append([0, 0, 0, 0, 0, 0, 0])

regionname = {}

def createBins():
    poroshenkoBins = [0.0]*101
    timoshenkoBins = [0.0]*101
    zelenskiyBins = [0.0]*101
    return [poroshenkoBins, timoshenkoBins, zelenskiyBins]

regions = {}
for i in range(-1, 100):
    regions[i] = createBins()

with open("data.csv", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        total = int(row[1])
        votes = int(row[6])
        poroshenko = int(row[39])
        timoshenko = int(row[45])
        zelenskiy = int(row[23])
        region = int(row[-2])
        regionname[region] = row[-1]
        assert poroshenko <= votes
        assert timoshenko <= votes
        assert zelenskiy <= votes
        aregion = regions[region]
        # print(total, votes, poroshenko, timoshenko, zelenskiy)
        if votes:
            poroshenkoRatio = float(poroshenko)/float(votes)
            timoshenkoRatio = float(timoshenko)/float(votes)
            zelenskiyRatio = float(zelenskiy)/float(votes)
            poroshenkoBin = int(100.0 * poroshenkoRatio)
            aregion[0][poroshenkoBin] += poroshenko
            timoshenkoBin = int(100.0 * timoshenkoRatio)
            aregion[1][timoshenkoBin] += timoshenko
            zelenskiyBin = int(100.0 * zelenskiyRatio)
            aregion[2][zelenskiyBin] += zelenskiy

bins = []
for i in range(101):
    bins.append(i)

for region in regions.keys():
    if region not in regionname:
        continue
    plt.clf()
    aregion = regions[region]
    plt.scatter(bins, aregion[0], color='red', s=7, label="Poroshenko")
    plt.scatter(bins, aregion[1], color='yellow', s=7, label="Timoshenko")
    plt.scatter(bins, aregion[2], color='green', s=7, label="Zelenskiy")
    plt.legend()
    plt.suptitle(regionname[region])
    plt.savefig("ptz.%s.png" % regionname[region], dpi=300)