# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:03:37 2019

@author: 최성국
"""
from matplotlib import pyplot as plt
import numpy as np
import math
from scipy.stats import pearsonr
f = open('../data/port_onedigit.txt','r')

lines=f.read().split('\n')
lines.pop()


year=[i for i in range(1962,2001)]
g=[[] for i in range(len(year))]
phi=[[[] for i in range(10)] for y in range(len(year))]

for each_line in lines:
    b=each_line.split()
    ye=year.index(int(b[0]))
    g[ye].append(float(b[2]))
    for p in range(10):
        phi[ye][p].append(float(b[p+3]))

slope_set=[[] for i in range(10)]

for y in range(len(year)):
    for p in range(10):
        non0_g=[]
        non0_p=[]
        for i in range(len(phi[y][p])):
            if g[y][i] >=pow(10,-3) and phi[y][p][i] !=0:
                non0_g.append(g[y][i])
                non0_p.append(phi[y][p][i])
        coeff=np.polyfit(np.log10(non0_g),np.log10(non0_p),1)
        slope_set[p].append(coeff[0])


marker=['o','x','s','>','^','v','*','<','3','1']
legend=['p=0','p=1','p=2','p=3','p=4','p=5','p=6','p=7','p=8','p=9']
color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
plt.figure(figsize=(10,5))
ax=plt.subplot(111)
for p in range(10):
    plt.plot(year,slope_set[p], marker=marker[p], color=color[p], label=legend[p], lw=3)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks( fontsize = 15)
plt.yticks( fontsize = 15)
plt.gcf().subplots_adjust(bottom=0.15, right=0.83)  
plt.xlim([1962,2000])
plt.xlabel('t(year)', size=15)
plt.ylabel('$\\alpha_p$', size=20)
plt.legend(loc='center left',  bbox_to_anchor=(1,0.65),frameon=False)

#plt.savefig('alpha_p-time.eps', format='eps', dpi=1000)