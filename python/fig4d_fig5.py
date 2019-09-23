# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:23:03 2018

@author: 최성국
"""

t1=['LEB','KUW','SAU','IRQ','LIB','VEN','IRN','TRI','OMA']
t2=['BUL','TAW','POL','CAO','EQG','DEN','IRE','SPN','MAG','ARG','SRI','GUA','MYA','TOG','SAL','HON','HAI','CAM','BRA','GHA','CDI','ETH','UGA','COL','CUB','ECU','COS','ICE','DOM','SOM','BFO']
t3=['DRC','CHL','AUS','JPN','BEL','HUN','YUG','POR','NOR','ISR','IND','CHN','FIN','CAN','PRK','PAN','SWD','GDR','NTH','ITA','FRN','CZE','USA','GFR','UKG']
t4=['MON','CHA','BOL','NIR','SUD','BUI','BEN','LBR','JOR','NEP','PAK','URU','AFG','SIE','MAL','CON','GAB']
t5=['TUR','GRC','SEN','JAM','PHI','MLI','TAZ','NIC','PAR','PER','SAF','CEN','MEX','ROK','MOR','AUL','MAA','CYP','THI','NEW','EGY','NIG','INS','ALB','SYR','TUN','RUM','RUS']
etc=['GUI','ALG']

g1962=[]
g1962.append(t1)
g1962.append(t2)
g1962.append(t3)
g1962.append(t4)
g1962.append(t5)
g1962a=[]

for x in g1962:
    for y in x:
        g1962a.append(y)

tt1=['IRQ','LIB','KUW','ALG','NIG','OMA','IRN','SAU','GAB','SUD','SYR','EQG','CON','VEN','NOR','NIR','TRI']
tt2=['ECU','CAO','DRC','RUS','EGY','COL']
tt3=['MON','TOG','AFG','MLI','GUI','BEN','BFO','PAR','JAM','CHA']
tt4=['NEP','HAI','CAM','SAL','HON','DOM','SRI']
tt5=['ICE','URU','NEW','GHA','TAZ','CHL','PER','ARG','BOL','AUL','SEN','UGA','ETH','CDI','BUI','SOM','MAA','CUB']
tt6=['BRA','COS','PAN','DEN','SPN','CYP','THI','SWD','GFR','FRN','UKG','SIE','MEX','ROK','TAW','USA','HUN','CAN','PRK','NTH','BEL','POL','ITA','POR','FIN','ISR','AUS','LBR','PHI','JPN','MAL']
tt7=['TUN','CHN','MOR','MYA','SAF','PAK','IND','YUG','INS','GRC','BUL','ALB','RUM','LEB','TUR']
etc2=['GUA','MAG','NIC','CEN','JOR','IRE']

g2000=[tt1,tt2,tt3,tt4,tt5,tt6,tt7]
g2000a=[]
for x in g2000:
    for y in x:
        g2000a.append(y)

from scipy.stats import pearsonr
#
from matplotlib import pyplot as plt
#
import numpy as np
#
import math
from matplotlib import colors


f = open('../data/portfolio5one-digit.txt','r')
lines=f.read().split('\n')
lines.pop()

year=[]
for i in range(1962,2001):
    year.append(i)
gdp=[[[0 for k in range(len(year))] for j in range(len(g2000))] for i in range(len(g1962))] 
numberofc=[[0 for j in range(len(g2000))] for i in range(len(g1962))]
gdp2000=[[0 for j in range(len(g2000))] for i in range(len(g1962))]
gdp1962=[[0 for j in range(len(g2000))] for i in range(len(g1962))]

gdp2000a=[0 for i in range(len(g2000))]
gdp1962a=[0 for i in range(len(g1962))]

for x in lines:
    b=x.split('\t')
    ye=year.index(int(b[0]))
    #if b[1] in etc or b[1] in etc2:
    #    pass
    if b[1] in g2000a and b[1] in g1962a:
        index1962=0
        index2000=0
        for i in range(len(g1962)):
            if b[1] in g1962[i]:
                index1962=int(i)
                break
        for j in range(len(g2000)):
            if b[1] in g2000[j]:
                index2000=int(j)
                break
        gdp[index1962][index2000][ye]=gdp[index1962][index2000][ye]+float(b[2])
        if int(b[0])==2000:        
            numberofc[index1962][index2000] +=1
            gdp2000[index1962][index2000]+= float(b[2])
            for g_n in range(len(g2000)):
                if b[1] in g2000[g_n] :
                    gdp2000a[g_n]+=float(b[2])
                    break
        if int(b[0])==1962:
            gdp1962[index1962][index2000] += float(b[2])
            for g_n in range(len(g1962)):
                if b[1] in g1962[g_n] :
                    gdp1962a[g_n]+=float(b[2])
                    break

ratio=[[[0 for k in range(len(year))] for j in range(len(g2000))] for i in range(len(g1962))]         
for i in range(len(gdp)):
    for j in range(len(gdp[i])):
        if sum(gdp[i][j]) != 0:
            for k in range(len(gdp[i][j])):
                ratio[i][j][k]=gdp[i][j][k]/gdp[i][j][0]
            
color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
c36=(np.array(colors.hex2color(colors.cnames['orange']))+np.array(colors.hex2color(colors.cnames['aqua'])))/2
c026=(np.array(colors.hex2color(colors.cnames['red']))*0.5)+(np.array(colors.hex2color(colors.cnames['pink']))*0.3)+(np.array(colors.hex2color(colors.cnames['aqua']))*0.2)
c76=(np.array(colors.hex2color(colors.cnames['aqua']))+np.array(colors.hex2color(colors.cnames['navy'])))/2
c87=(np.array(colors.hex2color(colors.cnames['darkcyan']))+np.array(colors.hex2color(colors.cnames['navy'])))/2
c20=(np.array(colors.hex2color(colors.cnames['red']))+np.array(colors.hex2color(colors.cnames['pink'])))/2

color=[ 'orange', c36,c20,'darkcyan',c026,c76,c87]
marker=['o','s','^','v','*']

legend62=['3','0','76','2','20']
legend00=['3','36','20','8','026','76','87']



def format_e(n):
    a = '%E' % n
    if float(a.split('E')[1]) >-3:
        return str(n)[:5]
    else:
        return a.split('E')[0].rstrip('0').rstrip('.')[:4] + 'E' + a.split('E')[1]

#plt.figure(figsize=(10,5))
for i in range(len(gdp)):
    plt.figure(figsize=(10,5))
    cnum=0
    
    for j in range(len(gdp[i])):
        if sum(ratio[i][j]) !=0:
            plt.plot(year,ratio[i][j],label=legend62[i]+' $\\rightarrow$ '+legend00[j] , color=color[j], marker=marker[i], lw=4, markersize=5)
            cnum+=1
            
    
    plt.xlabel('t(year)', size='20')
    plt.ylabel('g(C,t)', size='20')
    ax=plt.subplot(111)
    ax.legend(loc='center left',  bbox_to_anchor=(1,0.0+(1-(cnum*0.05))),frameon=False, fontsize=15)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.xticks( fontsize = 15)
    plt.yticks( fontsize = 15)
    #plt.gcf().subplots_adjust(bottom=0.13, right=0.83)
    plt.gcf().subplots_adjust(bottom=0.13,  right=0.71, left=0.10)
    #plt.yscale('log')
    plt.savefig('gdp_ratio_cluster'+str(i+1)+'2000.pdf', format='pdf', dpi=1000)







#color=['maroon','red','tomato', 'orangered', 'saddlebrown', 'olive', 'forestgreen','aqua','darkcyan','steelblue']


fig=plt.figure(figsize=(10,6.5))
check=0
for i in range(len(gdp)):
    
    for j in range(len(gdp[i])):
        if numberofc[i][j]>3:#and gdp1962[i][j] >=0.01:
            #plt.plot(year,ratio[i][j],label=str(i+1)+' $\\rightarrow$ '+str(j+1)+', '+str(numberofc[i][j])+', ' +str(gdp1962[i][j])[:5], color=color[check], marker=marker[check%8])
            plt.plot(year,ratio[i][j],label=legend62[i]+' $\\rightarrow$ '+legend00[j], color=color[j], marker=marker[i],lw=4, markersize=8)
            check+=1
#        if numberofc[i][j]>3 or gdp1962[i][j] >=0.01:
#            #plt.plot(year,ratio[i][j],label=str(i+1)+' $\\rightarrow$ '+str(j+1)+', '+str(numberofc[i][j])+', ' +str(gdp1962[i][j])[:5], color=color[check], marker=marker[check%8])
#            plt.plot(year,ratio[i][j],label=legend62[i]+' $\\rightarrow$ '+legend00[j], color=color[j], marker=marker[i],lw=4, markersize=8)
#            check+=1
        
plt.xlabel('t(year)', size='20')
plt.ylabel('g(C,t)', size='20')
ax=plt.subplot(111)
ax.legend(loc='center left',  bbox_to_anchor=(1,0.6),frameon=False, fontsize=15)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks( fontsize = 15)
plt.yticks( fontsize = 15)
plt.gcf().subplots_adjust(bottom=0.13, right=0.73, left=0.10)
plt.ylim([0.4,2.])
plt.savefig('fig5.pdf', format='pdf', dpi=1000)

#import pylab
#legend=['$\phi_{p=0}(C,t)$','$\phi_{p=1}(C,t)$','$\phi_{p=2}(C,t)$','$\phi_{p=3}(C,t)$','$\phi_{p=4}(C,t)$','$\phi_{p=5}(C,t)$','$\phi_{p=6}(C,t)$','$\phi_{p=7}(C,t)$','$\phi_{p=8}(C,t)$','$\phi_{p=9}(C,t)$']
#color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
#xxx=[1,2,3]
#yyy=[[i,i,i] for i in range(len(color))]
#fig=plt.figure()
#ax=plt.subplot(111)
#for i in range(len(color)):
#    plt.plot(xxx,yyy[i], c=color[i], lw=5, label=legend[i])
#plt.legend()
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)
#figLegend = pylab.figure()
#pylab.figlegend(*ax.get_legend_handles_labels(), loc='upper center', ncol=4,frameon=False)

import matplotlib.patches as mpatches

l1=mpatches.Patch(color='orange', label='g')
l2=mpatches.Patch(color='royalblue', label='N')

legend62=['3','0','76','2','20']
legend00=['3','36','2','8','026','76','87']
color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
#for i in range(len(group_port1962)):
#    fig=plt.figure()
#    plt.pie(group_port1962[i], colors=color)
    #plt.savefig('1962c'+str(i)+'.pdf', format='pdf', dpi=1000)
#for i in range(len(group_port2000)):
#    fig=plt.figure()
#    plt.pie(group_port2000[i], colors=color)
    #plt.savefig('2000c'+str(i)+'.pdf', format='pdf', dpi=1000)
c_len=[[],[]]

for x in g1962:
    c_len[0].append(len(x))
for x in g2000:
    c_len[1].append(len(x))
xax=np.arange(5)
xax2=np.arange(7)

fig=plt.figure(figsize=(10,5))
ax1=plt.subplot(111)
ax1.bar([i+0.3 for i in range(5)],gdp1962a, color='orange', edgecolor='orange')
ax1.set_ylabel('g',size=15, color='orange')
ax1.set_xlabel('Clusters in 1962', size=15)

ax2=ax1.twinx()
ax2.bar([i+0.3 for i in range(5)],c_len[0], width=0.2, color='royalblue',edgecolor='royalblue')    
ax2.set_ylabel('N',size=15, color='royalblue')

plt.xticks([i+0.3 for i in range(5)],['3','0','76','2','20'])
plt.legend(handles=[l1,l2], loc='upper right', bbox_to_anchor=(1.23,1), frameon=False )
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
plt.gcf().subplots_adjust(right=0.83, bottom=0.13)
plt.savefig('fig4d.pdf', format='pdf', dpi=1000)

############################################################
fig=plt.figure(figsize=(10,5))
ax1=plt.subplot(111)
ax1.bar([i+0.3 for i in range(7)],gdp2000a, color='orange', edgecolor='orange')
ax1.set_ylabel('g',size=15, color='orange')
ax1.set_xlabel('Clusters in 2000', size=15)

ax2=ax1.twinx()
ax2.bar([i+0.3 for i in range(7)],c_len[1], width=0.2, color='royalblue',edgecolor='royalblue')    
ax2.set_ylabel('N',size=15, color='royalblue')

plt.xticks([i+0.3 for i in range(7)],['3','36','20','8','026','76','87'])
plt.legend(handles=[l1,l2], loc='upper right', bbox_to_anchor=(1.23,1), frameon=False )
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
plt.gcf().subplots_adjust(right=0.83, bottom=0.13)
plt.savefig('fig4e.pdf', format='pdf', dpi=1000)