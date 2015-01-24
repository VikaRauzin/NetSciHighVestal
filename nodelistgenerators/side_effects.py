import csv
import os
os.chdir("..")
path_in = "meddra_freq_parsed.tsv"
path_out = "se_nodelist.csv"
with open(path_in, 'rb') as fin, open(path_out, 'wb') as fout:
    fin = csv.reader(fin, delimiter='\t')
    fout = csv.writer(fout)

    side_effects = dict()
    for line in fin:
        if line[3] in side_effects:  # checks whether side effect id is currently in the dictionary
            side_effects[line[3]] += 1  # if it is in the dictionary, increments frequency
        else:
            side_effects[line[3]] = 1  # if not in the dictionary, adds it with frequency of 1

    header = "Side Effect ID"  # gephi likes nodelists to have a header row
    fout.writerow([header])
    for s in sorted(set(side_effects.keys())):  # iterate dictionary keys, can be modified to include frequency
        row = s
        fout.writerow([row])