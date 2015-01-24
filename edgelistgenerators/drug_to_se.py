import csv
import os
os.chdir("..")  # moves working directory for data i/o to project master directory
path_in = "meddra_freq_parsed.tsv"
path_out = "se_edgelist.csv"
with open(path_in, 'rb') as fin, open(path_out, 'wb') as fout:
    fin = csv.reader(fin, delimiter='\t')
    fout = csv.writer(fout)
    edges = dict()
# dictionary format is ("DrugID", "SideEffectID"):freq sum, num of entries, placebo freq sum, num of placebo entries
# using low bound (line[7]) for frequency data for now, need to change
    for line in fin:
        e = line[0], line[3]  # key for new entry
        if e in edges:
            if line[5] != "placebo":  # adds to non-placebo values
                edges[e] += line[7], 1, 0, 0
            else:  # adds to placebo values
                edges[e] += 0, 0, line[7], 1
        else:
            if line[5] != "placebo":  # creates key and adds to non-placebo values
                edges[e] = line[7], 1, 0, 0
            else:  # creates key and adds to placebo values
                edges[e] = 0, 0, line[7], 1

    header = "Source", "Target", "Weight", "Type"
    fout.writerow(header)
    for edge, freq in sorted(set(edges.iteritems())):
        a, b, c, d = float(freq[0]), float(freq[1]), float(freq[2]), float(freq[3])
        if b == 0:
            b = 1.0  # ensures no division by zero
        if d == 0:
            d = 1.0  # ensures no division by zero

        weight = a / b - c / d  # subtracts mean placebo frequency from mean regular frequency
        if weight > 0:
            row = edge[0], edge[1], weight, "undirected"
            fout.writerow(row)