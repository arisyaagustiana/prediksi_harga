# inisialisasi
import numpy as np
import math
import pandas as pd
import csv

# Membaca excel
# 'training_pejati.csv'
training_p = input("Masukan file traning : ")
df1 = pd.read_csv(training_p)
# 'testing_pejati.csv'
testing_p = input("Masukan file testing : ")
df2 = pd.read_csv(testing_p)

training_count = df1.count(axis="rows")[0]
testing_count = df2.count(axis="rows")[0]
rows_count = df1.count(axis="columns")[0]

train = np.array(df1)
test = np.array(df2)

# Bobot korelasi
jml_bobot = input("Masukan jumlah bobot : ")
# 0.154, 0.221, 0.341, 0.108, 0.101, 0.076
bobot_p = []
for i in range(int(jml_bobot)):
	bobot = input("Bobot {} : ".format(i + 1))
	bobot_p.append(float(bobot))

# Mencari kesamaan nilai (retrieve): weight euclidean distance
nilai = []

for i in range(testing_count):
	for j in range(training_count):
		d_total = 0

		for k in range(rows_count - 1):
			kali_bobot = pow((test[i, k] - train[j, k]), 2) * bobot_p[k]
			d_total = d_total + kali_bobot

		nilai.append([math.sqrt(d_total), j])

nilai.sort(reverse=False)

with open('ed.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(0, len(nilai)):
		filewriter.writerow([nilai[i][0]])

min = nilai[0][0]
max = nilai[len(nilai) - 1][0]

# Mencari nilai normalisasi ed
normal = []
for i in range(len(nilai)):
	normal.append((nilai[i][0] - min) / (max - min))

with open('normalisasi.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(0, len(normal)):
		filewriter.writerow([normal[i]])
