# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:20:22 2019

@author: 최성국
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:05:33 2017

@author: 최성국
"""

import math
from scipy.stats import pearsonr
f = open('../data/port_onedigit.txt','r')
#g = open('C:/Users/최성국/Desktop/work/trade/data/777.txt','w')

lines=f.read().split('\n')
lines.pop()


a=[]
c=[]

a6=[]          #GDP
c6=[]          # Portion of particular product
a7=[]
c7=[]
a8=[]
c8=[]
a9=[]
c9=[]
a0=[]
c0=[]



year=[]
ctr=[]
a1=[]
#x=int(input('code:'))
#target product category
x=0
for each_line in lines:
    b=each_line.split()
    #a.append(float(b[5*x]))
    #a.append(float(b[2]))    #a.append(math.log(float(b[5*x])))
    a1.append(math.log(float(b[2] ),10))
    c.append(float(b[2*x+4]))
    year.append(b[0])
    ctr.append(b[1])
    each=0
    if int(b[0]) ==1962:
        a6.append(float(b[2]))
        c6.append(float(b[x+3]))
        #for p in range(x):
        #    each+=float(b[2*p+4])
        #c6.append(each)
    if int(b[0]) ==1970:
        a7.append(float(b[2]))
        c7.append(float(b[x+3]))
        #for p in range(x):
        #    each+=float(b[2*p+4])
        #c7.append(each)
    if int(b[0]) ==1980:
        a8.append(float(b[2]))
        c8.append(float(b[x+3]))
        #for p in range(x):
        #    each+=float(b[2*p+4])
        #c8.append(each)
    if int(b[0]) ==1990 :
        a9.append(float(b[2]))
        c9.append(float(b[x+3]))
        #for p in range(x):
        #    each+=float(b[2*p+4])
        #c9.append(each)
    if int(b[0]) ==2000 :
        a0.append(float(b[2]))
        c0.append(float(b[x+3]))
        #for p in range(x):
        #    each+=float(b[2*p+4])
        #c0.append(each)
        
        
        
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np


fig = plt.figure(figsize=(8.5,6))
#k=a.index(max(a))  #log일때는 미니멈
k=a1.index(min(a1))
k6=a6.index(min(a6))
k7=a7.index(min(a7))
#plt.scatter(a,c, c='grey', alpha='0.1')



n=10
#q=max(a)/n

base=np.logspace(np.log10(min(a6+a7+a8+a9+a0)), np.log10(max(a6+a7+a8+a9+a0)),n+1)
base2=[]
for i in range(n):
    base2.append((base[i]+base[i+1])/2)

x6=[]
y6=[]
yerr6=[]
yerr6a=[[],[]]
x7=[]
y7=[]
yerr7=[]
yerr7a=[[],[]]
x8=[]
y8=[]
yerr8=[]
yerr8a=[[],[]]
x9=[]
y9=[]
yerr9=[]
yerr9a=[[],[]]
x0=[]
y0=[]
yerr0=[]
yerr0a=[[],[]]

each_y6=[]
each_y0=[]
for i in range(n):
    g6=[]
    h6=[]
    for j in range(len(a6)):
        if a6[j] > base[i] and a6[j] <=base[i+1] and c6[j] !=0 :# c[j] !=0:   #log일때는 <=,>=
            g6.append(a6[j])
            h6.append(c6[j])
            
       
    if sum(h6)!=0:
        means=np.mean(np.log10(h6))
        var=np.std(np.log10(h6))/np.sqrt(len(h6))
        x6.append(np.log10(base2[i]))
        y6.append(np.mean(np.log10(h6)))
        yerr6.append(np.std(np.log10(h6))/np.sqrt(len(h6)))
        yerr6a[0].append(pow(10,means)-pow(10,means-var))
        yerr6a[1].append(pow(10,means+var)-pow(10,means))
    g7=[]
    h7=[]
    for j in range(len(a7)):
        if a7[j] > base[i] and a7[j] <=base[i+1] and c7[j] !=0 :# c[j] !=0:   #log일때는 <=,>=
            g7.append(a7[j])
            h7.append(c7[j])
            
           
    if sum(h7)!=0:
        means=np.mean(np.log10(h7))
        var=np.std(np.log10(h7))/np.sqrt(len(h7))
        x7.append(np.log10(base2[i]))
        y7.append(np.mean(np.log10(h7)))
        yerr7.append(np.std(np.log10(h7))/np.sqrt(len(h7)))
        yerr7a[0].append(pow(10,means)-pow(10,means-var))
        yerr7a[1].append(pow(10,means+var)-pow(10,means))
    g8=[]
    h8=[]
    for j in range(len(a8)):
        if a8[j] > base[i] and a8[j] <=base[i+1] and c8[j] !=0 :# c[j] !=0:   #log일때는 <=,>=
            g8.append(a8[j])
            h8.append(c8[j])
            
            
    if sum(h8)!=0:
        means=np.mean(np.log10(h8))
        var=np.std(np.log10(h8))/np.sqrt(len(h8))
        x8.append(np.log10(base2[i]))
        y8.append(np.mean(np.log10(h8)))
        yerr8.append(np.std(np.log10(h8))/np.sqrt(len(h8)))
        yerr8a[0].append(pow(10,means)-pow(10,means-var))
        yerr8a[1].append(pow(10,means+var)-pow(10,means))
    g9=[]
    h9=[]
    for j in range(len(a9)):
        if a9[j] > base[i] and a9[j] <=base[i+1] and c9[j] !=0 :# c[j] !=0:   #log일때는 <=,>=
            g9.append(a9[j])
            h9.append(c9[j])
            
            
    if sum(h9)!=0:
        means=np.mean(np.log10(h9))
        var=np.std(np.log10(h9))/np.sqrt(len(h9))
        x9.append(np.log10(base2[i]))
        y9.append(np.mean(np.log10(h9)))
        yerr9.append(np.std(np.log10(h9))/np.sqrt(len(h9)))
        yerr9a[0].append(pow(10,means)-pow(10,means-var))
        yerr9a[1].append(pow(10,means+var)-pow(10,means))
    g0=[]
    h0=[]
    for j in range(len(a0)):
        if a0[j] > base[i] and a0[j] <=base[i+1] and c0[j] !=0 :# c[j] !=0:   #log일때는 <=,>=
            g0.append(a0[j])
            h0.append(c0[j])
            
            
    if sum(h0)!=0:
        means=np.mean(np.log10(h0))
        var=np.std(np.log10(h0))/np.sqrt(len(h0))
        x0.append(np.log10(base2[i]))
        y0.append(np.mean(np.log10(h0)))
        yerr0.append(np.std(np.log10(h0))/np.sqrt(len(h0)))
        yerr0a[0].append(pow(10,means)-pow(10,means-var))
        yerr0a[1].append(pow(10,means+var)-pow(10,means))
co=2

coeff=np.polyfit(x0[2:],y0[2:],1)
yfit=lambda x:pow(x,coeff[0])*pow(10,coeff[1])*1.2
fig=plt.figure()
plt.xlabel('$g(c,t)$', size='20')
plt.ylabel('$\phi_'+str(x)+'(c,t)$', size='20')
plt.text(0.0, 0.9 , '(a)', fontsize=40, transform=plt.gcf().transFigure)


x6a=np.power(10,x6)
x7a=np.power(10,x7)
x8a=np.power(10,x8)
x9a=np.power(10,x9)
x0a=np.power(10,x0)

y6a=np.power(10,y6)
y7a=np.power(10,y7)
y8a=np.power(10,y8)
y9a=np.power(10,y9)
y0a=np.power(10,y0)

ax=plt.subplot(111)

plt.plot(x0a[2:],yfit(x0a[2:]), lw=10, ls='--', c='purple')
ax.scatter(x6a,y6a, marker='^', s=150, label='1962' , c='r')
plt.errorbar(x6a,y6a, yerr=yerr6a,  ecolor='red', color='red', ls='None')#,errorevery=5)
ax.scatter(x7a,y7a, marker='o', s=150, label='1970' , c='g')
plt.errorbar(x7a,y7a, yerr=yerr7a,  ecolor='g', color='g', ls='None')#,errorevery=5)
ax.scatter(x8a,y8a, marker='v', s=150, label='1980' , c='b')
plt.errorbar(x8a,y8a, yerr=yerr8a,  ecolor='b', color='b', ls='None')#,errorevery=5)
ax.scatter(x9a,y9a, marker='s', s=150, label='1990' , c='k')
plt.errorbar(x9a,y9a, yerr=yerr9a,  ecolor='black', color='black', ls='None')#,errorevery=5)
ax.scatter(x0a,y0a, marker='*', s=150, label='2000' , c='purple')
plt.errorbar(x0a,y0a, yerr=yerr0a,  ecolor='purple', color='purple', ls='None')#,errorevery=5)

plt.xlim([pow(10,-6),1])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_yscale('log')
ax.set_xscale('log')
ax.legend(loc='center left',  bbox_to_anchor=(1,0.8),frameon=False)#, fontsize='20' )
plt.gcf().subplots_adjust(bottom=0.11, right=0.74)
plt.xticks( fontsize = 13)
plt.yticks( fontsize = 13)
#plt.savefig('phi_9-g.eps', format='eps', dpi=1000)

