import csv
import os
os.chdir("..")  # moves working directory for data i/o to project master directory
path_in = "meddra_freq_parsed.tsv"
path_out = "se_edgelist.csv"
with open(path_in, 'rb') as fin, open(path_out, 'wb') as fout:
    fin = csv.reader(fin, delimiter='\t')
    fout = csv.writer(fout)
