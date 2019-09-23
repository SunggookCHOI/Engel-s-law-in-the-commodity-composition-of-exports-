# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:08:00 2018

@author: 최성국
"""

import math
from scipy.stats import pearsonr
import numpy as np
from matplotlib import pyplot as plt
f = open('../data/port_onedigit.txt','r')

lines=f.read().split('\n')
lines.pop()

era=[1962,2000]
phi_p_era=[[] for i in range(len(era))]
gdp_era=[[] for i in range(len(era))]
product=0

country=[[] for i in range(len(era))]

for line in lines:
    x=line.split('\t')
    if int(x[0]) == 1962:
        phi_p_era[0].append(float(x[product+3]))
        gdp_era[0].append(float(x[2]))
        country[0].append(x[1])
    if int(x[0]) == 2000 and x[1] in country[0]:
        phi_p_era[1].append(float(x[product+3]))
        gdp_era[1].append(float(x[2]))
        country[1].append(x[1])

phi_ratio=[]
g_ratio=[]



ROK=[]
TAW=[]
CHN=[]
INS=[]

for i in range(len(country[0])):
    if country[0][i] in country[1] and gdp_era[0][i] !=0 and phi_p_era[0][i] !=0 and phi_p_era[1][country[1].index(country[0][i])] !=0:
        phi_ratio.append(phi_p_era[1][country[1].index(country[0][i])]/phi_p_era[0][i])
        g_ratio.append(gdp_era[1][country[1].index(country[0][i])]/gdp_era[0][i])
        if country[0][i] =='ROK':
            ROK.append(phi_p_era[1][country[1].index(country[0][i])]/phi_p_era[0][i])
            ROK.append(gdp_era[1][country[1].index(country[0][i])]/gdp_era[0][i])
        if country[0][i] =='TAW':
            TAW.append(phi_p_era[1][country[1].index(country[0][i])]/phi_p_era[0][i])
            TAW.append(gdp_era[1][country[1].index(country[0][i])]/gdp_era[0][i])
        if country[0][i] =='CHN':
            CHN.append(phi_p_era[1][country[1].index(country[0][i])]/phi_p_era[0][i])
            CHN.append(gdp_era[1][country[1].index(country[0][i])]/gdp_era[0][i])
        if country[0][i] =='INS':
            INS.append(phi_p_era[1][country[1].index(country[0][i])]/phi_p_era[0][i])
            INS.append(gdp_era[1][country[1].index(country[0][i])]/gdp_era[0][i])
        


binn=10
base=np.logspace(np.log10(min(phi_ratio)), np.log10(max(phi_ratio)),binn)
base[-1]=base[-1]+1
interval=[[] for i in range(binn-1)]

base2=[]
for i in range(binn-1):
    base2.append((base[i]+base[i+1])/2)
    
log_g=[]
log_phi=[]
for i in range(len(g_ratio)):
    if g_ratio[i] !=0 and phi_ratio[i] !=0:
        log_g.append(np.log(g_ratio[i]))
        log_phi.append(np.log(phi_ratio[i]))
        for j in range(binn-1):
            if phi_ratio[i]>=base[j] and phi_ratio[i]<base[j+1]:
                interval[j].append(g_ratio[i])#np.log(phi_ratio[i]))
                break
interval_mean=[]
yerr=[[],[]]
point_num=[0,0]

for x in interval:
    mean=np.mean(np.log10(x))
    var=np.std(np.log10(x))
    interval_mean.append(pow(10,mean))
    yerr[0].append(pow(10,mean)-pow(10,mean-var))
    yerr[1].append(pow(10,mean+var)-pow(10,mean))
fig=plt.figure()
ax=plt.subplot(111)

for i in range(len(phi_ratio)):
    if phi_ratio[i] >=1:
        plt.scatter(phi_ratio[i], g_ratio[i],s=80, facecolor='red', edgecolor='red')
        point_num[0]+=1
    else:
        plt.scatter(phi_ratio[i], g_ratio[i],s=80, facecolor='skyblue', edgecolor='skyblue')
        point_num[1] +=1
plt.plot(base2,interval_mean)
plt.errorbar(base2,interval_mean, yerr=yerr, capsize=5, c='k')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('$g(c,2000)/g(c,1962)$', size=20)
plt.xlabel('$\phi_'+str(product)+'(c,2000)$/'+'$\phi_'+str(product)+'(c,1962)$', size=20)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.gcf().subplots_adjust(bottom=0.13)#, right=0.79)
plt.ylim([0.05,10.5])
#plt.savefig('phi_'+str(product)+'vs_g(ratio).eps', format='eps', dpi=1000)#plt.xlim([0.07,12])
#plt.ylim([0.003,46])
ax.annotate('South Korea', xy=(ROK[0], ROK[1]), xytext=(ROK[0]/5, ROK[1]/2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('Taiwan', xy=(TAW[0], TAW[1]), xytext=(TAW[0]*2, TAW[1]+3),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('China', xy=(CHN[0], CHN[1]), xytext=(CHN[0]*3, CHN[1]*3),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('Indonesia', xy=(INS[0], INS[1]), xytext=(INS[0]*2, INS[1]*3),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )            

print(pearsonr(log_g, log_phi))
print('>1, <1', np.array(point_num)/sum(point_num))
plt.text(0.0, 0.9 , '(a)', fontsize=35, transform=plt.gcf().transFigure)
#plt.savefig('phi_'+str(product)+'vs_g(ratio)a.eps', format='eps', dpi=1000)







#######################################
reliable=[]
reliable2=[]
for i in range(11):
    
    reliable.append(np.sqrt(4/(len(g_ratio)-2+4)))
    reliable2.append(-np.sqrt(4/(len(g_ratio)-2+4)))

pv=[-0.25350786114042967,-0.11502177667982622, -0.27597546185477984,-0.18554939830770148, 0.054437488166280024,0.052596462041629925, -0.02611800714572745
,0.19008615297243844,0.06525106725689823, -0.1252105930492075]
legend=['p=0','p=1','p=2','p=3','p=4','p=5','p=6','p=7','p=8','p=9']

xax=[i-0.5 for i in range(10)]
fig=plt.figure()
ax=plt.subplot(111)
plt.bar(xax,pv,color='None', edgecolor='blue', lw=5)
ax.fill_between(xax+[9.5],reliable,reliable2, facecolor='grey', alpha=0.2)
plt.xlim([-0.5,9.5])
plt.ylim([-0.3,0.3])
plt.xticks([0,1,2,3,4,5,6,7,8,9])
plt.xlabel('p', size=15)
plt.ylabel('$\\rho(\{g(c,2000),g(c,1962)\},\{\phi_p(c,2000)/\phi_p(c,1962)\})$', size=15)
#plt.savefig('pcc_ratio.pdf', format='pdf', dpi=1000)



asdf=[[0.20183486, 0.79816514],[0.40789474, 0.59210526],[0.12727273, 0.87272727],[0.68181818, 0.31818182],[0.22368421, 0.77631579],[0.77227723, 0.22772277],[0.64814815, 0.35185185],[0.80733945, 0.19266055],[0.8317757, 0.1682243],[0.80373832, 0.19626168]]
asdf=np.array(asdf).T.tolist()
fig=plt.figure()
ax=plt.subplot(111)
b=[0 for yy in range(10)]
legend=['$\phi_p \over{\phi_p}$','${\phi_p} \over{\phi_p}$']
color=['r','skyblue']
for i in range(2):
    plt.bar(xax,asdf[i],bottom=b, color=color[i])#, label=legend[i])
    for j in range(10):
        b[j]=b[j]+asdf[i][j]
plt.xlabel('t(year)', size='15')
plt.xlim([-0.7,9.5])
plt.xticks([0,1,2,3,4,5,6,7,8,9])
plt.ylabel('Ratio', size=15)
#ax.legend(loc='center left',  bbox_to_anchor=(1,0.7),frameon=False)
#plt.legend()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
#plt.savefig('ratio_data_point.eps', format='eps', dpi=1000)