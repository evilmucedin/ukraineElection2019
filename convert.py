#!/usr/bin/env python3

import os
import csv

headerPrinted = False

def main():
    outCsv = csv.writer(open("data.csv", "w"))

    for i in range(300):
        filename = "webArchive/%d.html" % i
        if not os.path.isfile(filename):
            continue

        def writeRow(row):
            global headerPrinted
            if len(row) != 0:
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
