# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:10:21 2017

@author: mucs_b
"""
import random
import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt

class generator():
    def  __init__(self,mean,stdev):
        self.fnkt = st.norm(mean,stdev)
        
    def generate_random_number(self):
        return(np.round(self.fnkt.rvs(),2))

    def ppf(self,ninp):
        return(self.fnkt.ppf(ninp))
    
    def cdf(self,ninp):
        return(self.fnkt.cdf(ninp))

    def show(self):
        plt.hist(self.fnkt.rvs(10000),bins = 50)
        plt.title('Chances for scores')
        plt.show()
        
cmean = random.randint(0,100)
cstdev = random.randint(0,100)
myrandomgen = generator(cmean,cstdev)        
cRange = random.randint(3,15)

myrandomgen
slist = []
depth = 0
for i in range(1,cRange+1):
    
    pScore = myrandomgen.generate_random_number()
    
    slist.append(pScore)
    if depth == cRange-1:
        break
    plt.plot(slist)
    plt.show()
    while True:
        X = input('Current score: '+str(pScore) + '. You have '+str(cRange-i)+' tries left.'+' Continue (y/n)?')
        if X == 'y':
            depth += 1
            break
        if X == 'n':
            break
        print('Input error! Input "y" for "yes" any "n"  for "no".' )
    if X == 'n':
        break
    
    
print('Congrats. Your final score is: ' + str(pScore))

for i2 in range(cRange-1-depth):
    slist.append(myrandomgen.generate_random_number())

tmax = max(slist)
lmax = max(slist[:depth+1])
print('Best possible score you could have gotten: '+str(tmax))

stopped_on_local_maximum = slist[:depth+1][-1] == max(slist[:depth+1])

print('Stopped on local maximum: '+str(stopped_on_local_maximum))

tchance = np.round((100-myrandomgen.cdf(pScore)*100)*(cRange-1-depth),2)
lchance = np.round((100-myrandomgen.cdf(lmax)*100)*(cRange-1-slist.index(lmax)),2)

if depth >= cRange-1:
    print('You never stopped!')
else:
    print('You had a '+ str(tchance)+'% chance to get a better score when you stopped!')

print('You had a '+ str(lchance)+'% chance to get a better score when you encountered your highest score!')


try:
    best_dif_before_stop = max([i-myrandomgen.ppf(1-1/(len(slist)-(slist.index(i)))) for i in slist[0:depth]])
except(ValueError):
    best_dif_before_stop = None

try:
    dif_when_stop = myrandomgen.ppf(1-1/(len(slist)-(slist.index(slist[depth]))))-slist[depth]
except(IndexError):
    dif_when_stop =None

best_dif_before_stop == None

if best_dif_before_stop == None:
    print('Irrac index: '+str(round(dif_when_stop/cmean,2)))
elif depth >= cRange-1:
    print('Irrac index:'+str(round(best_dif_before_stop/cmean,2)))
else:
    print('Irrac index: '+str(round(max(best_dif_before_stop,dif_when_stop)/cmean,2)))
    
print('Depth: '+ str(round(depth/(cRange-1)*100,2))+'%')

myrandomgen.show()
