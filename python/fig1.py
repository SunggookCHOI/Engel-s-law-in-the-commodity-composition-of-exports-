# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:13:51 2017

@author: 최성국
"""
from matplotlib import pyplot as plt

f = open('../data/Export_from_wtf.txt','r')

lines=f.read().split('\n')
lines.pop()


year=[]
for i in range(1962,2001):
    year.append(i)
    
product=['0','1','2','3','4','5','6','7','8','9']
port=[[0 for x in range(10)] for y in range(len(year))]

for x in lines:
    b=x.split('\t')
    if int(b[0]) in year and len(b[3])==4 and b[2] == 'World':                 #for all country
        ye=year.index(int(b[0]))
        k=product.index(b[3][0])
        port[ye][k]=port[ye][k]+float(b[4])

n_port=[[] for i in range(len(product))]

for i in range(len(port)):
    
    for j in range(len(port[i])):
        n_port[j].append(port[i][j]/sum(port[i]))
    
    

plt.figure(figsize=(10,5))
marker=['o','x','+','>','^','v','*','','.','1']
legend=['p=0','p=1','p=2','p=3','p=4','p=5','p=6','p=7','p=8','p=9']
color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
hatch=['','','x','/','|','\\','o','','/','']




fig=plt.figure()
b=[0 for yy in range(len(year))]
n_port.reverse()
color.reverse()
hatch.reverse()
legend.reverse()
for i in range(len(product)):
    plt.bar(year,n_port[i],bottom=b, color=color[i], label=legend[i], hatch=hatch[i])
    for j in range(len(year)):
        b[j]=b[j]+n_port[i][j]
plt.xlabel('t(year)', size='20')
plt.ylabel('<$\phi_p$>(t)', size='20')
ax=plt.subplot(111)

plt.ylim([0,1])
handles, labels = ax.get_legend_handles_labels()

ax.legend(handles[::-1], labels[::-1], loc='center left',  bbox_to_anchor=(1,0.7),frameon=False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks([1962,1965,1970,1975,1980,1985,1990,1995,2000],['1962     ',1965,1970,1975,1980,1985,1990,1995,2000], fontsize = 15)
plt.yticks( fontsize = 15)
plt.gcf().subplots_adjust(bottom=0.13, right=0.83)
plt.xlim([1962,2000])
#plt.savefig('mean_phi-time.eps', format='eps', dpi=1000)

