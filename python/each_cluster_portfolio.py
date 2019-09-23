# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:49:56 2019

@author: 최성국
"""

#######threshold=0.485#############

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
#g1962.append(etc)
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

#############################################

code=['0','1','2','3','4','5','6','7','8','9']

from matplotlib import pyplot as plt

import numpy as np
cluster1=t1
cluster2=t2
cluster3=t3
cluster4=t4
cluster5=t5
#cluster6=tt6
#cluster7=tt7
f = open('../data/port_onedigit.txt','r')

lines=f.read().split('\n')
lines.pop()

group_port1962=[[0 for j in range(10)] for i in range(5)]  #[g1962][g2000][product code]
group_port2000=[[0 for j in range(10)] for i in range(7)]


for line in lines:
    b=line.split('\t')
    if b[1] in g1962a and int(b[0]) ==1962:
        for i in range(len(g1962)):
            g_index=0
            for group in range(len(g1962)):
                if b[1] in g1962[group]:
                    g_index=group
                    break
            for p in range(10):
                group_port1962[g_index][p]+=float(b[p+3])
    if b[1] in g2000a and int(b[0]) ==2000:
        for i in range(len(g2000)):
            g_index=0
            for group in range(len(g2000)):
                if b[1] in g2000[group]:
                    g_index=group
                    break
            for p in range(10):
                group_port2000[g_index][p]+=float(b[p+3])

legend62=['3','0','76','2','20']
legend00=['3','36','2','8','026','76','87']
color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
for i in range(len(group_port1962)):
    fig=plt.figure()
    plt.pie(group_port1962[i], colors=color)
    #plt.savefig('1962c'+str(i)+'.pdf', format='pdf', dpi=1000)
for i in range(len(group_port2000)):
    fig=plt.figure()
    plt.pie(group_port2000[i], colors=color)
    #plt.savefig('2000c'+str(i)+'.pdf', format='pdf', dpi=1000)
c_len=[[],[]]

for x in g1962:
    c_len[0].append(len(x))
for x in g2000:
    c_len[1].append(len(x))
    