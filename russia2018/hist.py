#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

putinBins = [0]*101
with open("table_227_level_3.tsv", "r") as f:
    next(f)
    for line in f:
        row = line.strip().split("\t")
        total = int(row[3])
        votes = int(row[12])
        putin = int(row[18])
        # print(total, votes, putin)
        assert votes <= total
        assert putin <= votes
        if votes:
            turnover = float(votes)/total
            putinRatio = float(putin)/float(votes)
            putinBin = int(100.0 * putinRatio)
            putinBins[putinBin] += putin

abins = []
for i in range(101):
    abins.append(i)

plt.clf()
plt.plot(abins, putinBins, color='red', label="Putin")
plt.legend()
plt.suptitle("Russia")
plt.savefig("pAll.png", dpi=300)
plt.show()
