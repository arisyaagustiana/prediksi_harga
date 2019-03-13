#inisialisasi
import numpy
import math
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import xlsxwriter

#Membaca excel
training_p = r'data/training_pejati.xlsx'
df1 = pd.read_excel('training_p)
testing_p = r'data/testing_pejati.xlsx'
df2 = pd.read_excel('testing_p)

#Bobot korelasi
bobot_p = [0,154 0,221 0,341 0,108 0,101 0,076]

#n (variabel bebas) = 6

#Mencari kesamaan nilai (retrieve): weight euclidean distance
for i in range(testing_p):
    for j in range(training_p):
	dtotal_p = 0
       for k in range(1, n):	
		distance(i,j) = pow((testing_p[(i,k)]) - (training_p[(j,k)]),2)
		kali(k) = distance(i,j) * bobot_p(k)
		dtotal_p = d_total + kali(k)
	return dtotal_p, math.sqrt(dtotal_p)

#Mengurutkan nilai ed dari kecil ke besar
	print dtotal_p.sort(reverse=False)

#tentukan lokasi file, nama file dan inisialisasi xlsx
	workbook = xlsxwriter.Workbook('dtotal_p.xlsx')
	worksheet = workbook.add_worksheet('dpejati')

	datadpejati = 'dtotal_p'
	row = 0

#menulis file
	for co1, data in enumerate(datadpejati):
		worksheet.write_colomn(row, co1, data)

#menutup file xlsx
	workbook.close()
return
return