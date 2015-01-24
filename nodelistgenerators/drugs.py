# unnecessary because we have an edgelist generator

import csv
import os
os.chdir("..")  # moves working directory for data i/o to project master directory
path_in = "meddra_freq_parsed.tsv"
path_out = "drug_nodelist.csv"
with open(path_in, 'rb') as fin, open(path_out, 'wb') as fout:
    fin = csv.reader(fin, delimiter='\t')
    fout = csv.writer(fout)

    drugs = dict()
    for line in fin:
        if line[0] in drugs:  # checks whether drug id is currently in the dictionary
            drugs[line[0]] += 1  # if it is in the dictionary, increments frequency
        else:
            drugs[line[0]] = 1  # if not in the dictionary, adds it with frequency of 1

    header = "Drug ID"  # gephi likes nodelists to have a header row
    fout.writerow([header])
    for d in sorted(set(drugs.keys())):  # iterate dictionary keys, can be modified to include frequency
        row = d
        fout.writerow([row])
