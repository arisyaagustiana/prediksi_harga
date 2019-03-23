# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 02:28:58 2019

@author: user
"""

from random import random
from math import exp

#Evaluasi solusi: Revise 
#Data yang digunakan yaitu data training 70%
training_p = input("Masukan file training : ")
df1 = pd.read_csv(training_p)        
training_count = df1.count(axis="rows")[0]        
train = np.array(df1)        
        
#Selisih acak 2 data
#mencari beberapa pasangan untuk memenuhi epoch maksimal        

with open('training_JST.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(0, len(normal)):
		filewriter.writerow([normal[i]])
        
def init (self, n_input, n_hidden, n_output):
    self.n_input = input + 1   #inisialisasi n_input = bias 
    self.n_hidden = hidden      #inisialisasi hidden layer
    self.n_output = output      #inisialisasi output layer
    
    #inisialisasi bobot matrix antara input layer dan hidden layer
    self.input_bobot = random.rand(self.n_input, self.n_hidden)
    #inisialisasi bobot matrix antara hidden layer dan output layer
    self.output_bobot = random.rand(self.n_hidden, self.n_output)
    
    self.alpha = 0.5    #inisialisasi learning rate
    self.epoch = 10000  #inisialisasi max epoch
    
    def n_aktivasi(self, n_input):
        for n_input in range(self.n_input - 1):
            sum += self.n_input + df1*self.input_bobot
            for n_hidden in range(self.hidden):
                sum = 0.0
            
            
            
            
#Menghitung neuron aktivasi untuk sebuah input
def n_aktivasi(bobot, input):
z_hidden[]

    z_net = bobot[-1]
    for i in range(len(bobot)-1):
         z_net += bobot[i] * input[i] #input=row dari data training
    
    z_hidden.append(float(z_hidden))
    return z_net

#Transfer neuron aktivasi (Sigmoid Biner)
def transfer(z_net):
    return 1/(1 + exp(-z_net))

#Transfer neuron aktivasi (Identitas)
def transfer_identitas(z_net):
    return z_net
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    