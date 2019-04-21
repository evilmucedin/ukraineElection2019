#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

bins = []
for i in range(101):
    bins.append([0, 0, 0, 0, 0, 0, 0])

NBINS = 50

poroshenkoBins = [0.0]*(NBINS + 1)
zelenskiyBins = [0.0]*(NBINS + 1)
poroshenkoTurnoutBins = [0.0]*(NBINS + 1)
zelenskiyTurnoutBins = [0.0]*(NBINS + 1)

fPoroshenko = open("poroshenko.tsv", "w")
fZelenskiy = open("zelenskiy.tsv", "w")

aturnout = []
aporoshenko = []
azelenskiy = []
with open("data.csv", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader)
    for row in csvReader:
        total = int(row[1])
        votes = int(row[6])
        poroshenko = int(row[11])
        zelenskiy = int(row[10])
        assert votes <= total
        assert poroshenko <= votes
        assert zelenskiy <= votes
        # print(total, votes, poroshenko, zelenskiy)
        if votes:
            turnout = float(votes)/total
            aturnout.append(turnout)
            aporoshenko.append(poroshenko)
            azelenskiy.append(zelenskiy)
            print(turnout, poroshenko, file=fPoroshenko)
            print(turnout, zelenskiy, file=fZelenskiy)
            poroshenkoRatio = float(poroshenko)/float(votes)
            zelenskiyRatio = float(zelenskiy)/float(votes)
            bn = int(turnout * 100.)
            bins[bn][0] += 1
            bins[bn][1] += poroshenko
            bins[bn][2] += zelenskiy
            bins[bn][3] += poroshenkoRatio
            bins[bn][4] += zelenskiyRatio
            turnoutBin = int(float(NBINS) * turnout)
            poroshenkoBin = int(float(NBINS) * poroshenkoRatio)
            poroshenkoBins[poroshenkoBin] += poroshenko
            poroshenkoTurnoutBins[turnoutBin] += poroshenko
            zelenskiyBin = int(float(NBINS) * zelenskiyRatio)
            zelenskiyBins[zelenskiyBin] += zelenskiy
            zelenskiyTurnoutBins[turnoutBin] += zelenskiy

plt.scatter(aturnout, aporoshenko, color='red', s=7, label="Poroshenko")
plt.scatter(aturnout, azelenskiy, color='green', s=7, label="Zelenskiy")
plt.xlabel("Turnout")
plt.ylabel("#Votes")
plt.legend()
plt.savefig("ptz.png", dpi=300)
plt.show()

abins = []
for i in range(NBINS + 1):
    abins.append(i*(100.0)/NBINS)

plt.plot(abins, poroshenkoTurnoutBins, color='red', label="Poroshenko")
plt.plot(abins, zelenskiyTurnoutBins, color='green', label="Zelenskiy")
plt.xlabel("Turnout")
plt.ylabel("#Votes")
plt.legend()
plt.savefig("ptzTurnout.png", dpi=300)
plt.show()

plt.clf()
plt.plot(abins, poroshenkoBins, color='red', label="Poroshenko")
plt.plot(abins, zelenskiyBins, color='green', label="Zelenskiy")
plt.legend()
plt.xlabel("Votes% for the candidate")
plt.ylabel("#Votes")
plt.suptitle("Ukraine")
plt.savefig("ptzAll.png", dpi=300)
plt.show()

with open("pt.tsv", "w") as f:
    for i in range(NBINS + 1):
        if bins[i][0]:
            print(i, bins[i][0]*100., bins[i][1], bins[i][2], bins[i][3], bins[i][4]/bins[i][0], bins[i][5]/bins[i][0], file=f)

with open("p.tsv", "w") as f:
    for i in range(NBINS + 1):
        print(i, poroshenkoBins[i], zelenskiyBins[i], file=f)
