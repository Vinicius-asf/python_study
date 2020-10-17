import csv
from sklearn import metrics
import numpy as np

y_pred = []
y_true = []

with open('reconhecimeto.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    r_count = 0
    for row in spamreader:
        if r_count == 0:
            print(row)
            r_count+=1
        else:
            y_true.append(row[0])
            y_pred.append(row[1])

cnf_mtx = metrics.confusion_matrix(y_true,y_pred)

print(1)

with open('confusion_result.csv', mode='w',newline='') as conf_res:
    spamwriter = csv.writer(conf_res, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in cnf_mtx:
        spamwriter.writerow(row)