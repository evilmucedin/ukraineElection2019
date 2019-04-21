#!/usr/bin/env python3

import os
import csv

headerPrinted = False

region = {}
regionname = {}

index = 0
def m(s, b, e):
    global index
    for i in range(b, e + 1):
        region[i] = index
        regionname[i] = s
    index += 1

m("Vinnitsa", 11, 18)
m("Volyn", 19, 23)
m("Dnepr", 24, 40)
m("Donetsk", 45, 60)
m("Zhitomir", 62, 67)
m("Zakarpatie", 68, 73)
m("Zaporozhie", 74, 82)
m("Ivano-Frankovsk", 83, 89)
m("Kiev", 90, 98)
m("Kirov", 99, 103)
m("Lugansk", 105, 114)
m("Lvov", 115, 126)
m("Nikolaev", 127, 132)
m("Odessa", 133, 143)
m("Poltava", 144, 151)
m("Rovno", 152, 156)
m("Sumy", 157, 162)
m("Ternopol", 163, 167)
m("Harkov", 168, 181)
m("Herson", 182, 186)
m("Hmelnitsk", 187, 193)
m("Cherkassy", 194, 200)
m("Chernovtsy", 201, 204)
m("Chernigov", 205, 210)
m("Kiev (city)", 211, 223)

def main():
    outCsv = csv.writer(open("data.csv", "w"))

    for i in range(300):
        filename = "webArchive/%d.html" % i
        if not os.path.isfile(filename):
            continue

        def writeRow(row):
            global headerPrinted
            if len(row) != 0:
                row.append(str(i))
                if i in region:
                    row.append(region[i])
                    row.append(regionname[i])
                else:
                    row.append("-1")
                    row.append("")
                isHeader = not row[0].isdigit()
                if isHeader:
                    if not headerPrinted:
                        outCsv.writerow(row)
                        headerPrinted = True
                else:
                    outCsv.writerow(row)

        row = []
        for line in open(filename):
            line = line.strip()

            if line.startswith("<th class=\"row-fixed\">") or line.startswith("<td class=\"cntr\">"):
                value = line[line.find(">") + 1:len(line)]
                value = value.replace("<br>", " ")
                row.append(value)

            if line.startswith("</tr>") or line.startswith("</th>") or line.startswith("<tr>"):
                writeRow(row)
                row = []

        writeRow(row)
        print(i)

if __name__ == "__main__":
    main()
