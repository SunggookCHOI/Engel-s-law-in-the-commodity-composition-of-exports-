f = open('../data/port_onedigit.txt','r')
#g = open('C:/Users/최성국/Desktop/work/trade/data/연도별pearsonr(g,phi7).txt','w')



#######threshold=0.485#############
t1=['LEB','KUW','SAU','IRQ','LIB','VEN','IRN','TRI','OMA']
t2=['BUL','TAW','POL','CAO','EQG','DEN','IRE','SPN','MAG','ARG','SRI','GUA','MYA','TOG','SAL','HON','HAI','CAM','BRA','GHA','CDI','ETH','UGA','COL','CUB','ECU','COS','ICE','DOM','SOM','BFO']
t3=['DRC','CHL','AUS','JPN','BEL','HUN','YUG','POR','NOR','ISR','IND','CHN','FIN','CAN','PRK','PAN','SWD','GDR','NTH','ITA','FRN','CZE','USA','GFR','UKG']
t4=['MON','CHA','BOL','NIR','SUD','BUI','BEN','LBR','JOR','NEP','PAK','URU','AFG','SIE','MAL','CON','GAB']
t5=['TUR','GRC','SEN','JAM','PHI','MLI','TAZ','NIC','PAR','PER','SAF','CEN','MEX','ROK','MOR','AUL','MAA','CYP','THI','NEW','EGY','NIG','INS','ALB','SYR','TUN','RUM','RUS']
etc=['GUI','ALG']

country=['LEB', 'KUW', 'SAU', 'IRQ', 'LIB', 'VEN', 'IRN', 'TRI', 'OMA', 'BUL', 'TAW', 'POL', 'CAO', 'EQG', 'DEN', 'IRE', 'SPN', 'MAG', 'ARG', 'SRI', 'GUA', 'MYA', 'TOG', 'SAL', 'HON', 'HAI', 'CAM', 'BRA', 'GHA', 'CDI', 'ETH', 'UGA', 'COL', 'CUB', 'ECU', 'COS', 'ICE', 'DOM', 'SOM', 'BFO', 'DRC', 'CHL', 'AUS', 'JPN', 'BEL', 'HUN', 'YUG', 'POR', 'NOR', 'ISR', 'IND', 'CHN', 'FIN', 'CAN', 'PRK', 'PAN', 'SWD', 'NTH', 'ITA', 'FRN', 'USA', 'GFR', 'UKG', 'MON', 'CHA', 'BOL', 'NIR', 'SUD', 'BUI', 'BEN', 'LBR', 'JOR', 'NEP', 'PAK', 'URU', 'AFG', 'SIE', 'MAL', 'CON', 'GAB', 'TUR', 'GRC', 'SEN', 'JAM', 'PHI', 'MLI', 'TAZ', 'NIC', 'PAR', 'PER', 'SAF', 'CEN', 'MEX', 'ROK', 'MOR', 'AUL', 'MAA', 'CYP', 'THI', 'NEW', 'EGY', 'NIG', 'INS', 'ALB', 'SYR', 'TUN', 'RUM', 'GUI', 'ALG']


print(len(country))

tt1=['IRQ','LIB','KUW','ALG','NIG','OMA','IRN','SAU','GAB','SUD','SYR','EQG','CON','VEN','NOR','NIR','TRI']
tt2=['ECU','CAO','DRC','RUS','EGY','COL']
tt3=['MON','TOG','AFG','MLI','GUI','BEN','BFO','PAR','JAM','CHA']
tt4=['NEP','HAI','CAM','SAL','HON','DOM','SRI']
tt5=['ICE','URU','NEW','GHA','TAZ','CHL','PER','ARG','BOL','AUL','SEN','UGA','ETH','CDI','BUI','SOM','MAA','CUB']
tt6=['BRA','COS','PAN','DEN','SPN','CYP','THI','SWD','GFR','FRN','UKG','SIE','MEX','ROK','TAW','USA','HUN','CAN','PRK','NTH','BEL','POL','ITA','POR','FIN','ISR','AUS','LBR','PHI','JPN','MAL']
tt7=['TUN','CHN','MOR','MYA','SAF','PAK','IND','YUG','INS','GRC','BUL','ALB','RUM','LEB','TUR']
etc2=['GUA','MAG','NIC','CEN','JOR','IRE']
country2=tt1+tt2+tt3+tt4+tt5+tt6+tt7+etc2

for x in country2 :
    if x not in country:
        print(x)
#############################################
code=['0','1','2','3','4','5','6','7','8','9']
lines=f.read().split('\n')
lines.pop()
phi=[[[] for x in range(len(code))] for y in range(39)]
gdp=[[] for y in range(39)]

from scipy.stats import pearsonr
import numpy as np
from matplotlib import pyplot as plt

for x in lines:
    b=x.split('\t')
    gdp[int(b[0])-1962].append(float(b[2]))
    for k in range(len(code)):
        phi[int(b[0])-1962][k].append(float(b[k+3]))

pcc=[[] for x in range(len(code))]
pvalue=[[] for x in range(len(code))]
year=[]

for i in range(1962,2001):
    year.append(i)
    for x in range(len(code)):
        pcc[x].append(pearsonr(phi[i-1962][x],gdp[i-1962])[0])
        pvalue[x].append(pearsonr(phi[i-1962][x],gdp[i-1962])[1])

#for x in range(len(code)):
#    print(x, sum(pcc[x])/len(pcc[x]), sum(pvalue[x])/len(pvalue[x]))


# Calculate region which p-value of pearsonr is larger than 0.05
data_num=[]
for i in range(len(phi)):
    data_num.append(len(phi[i][0]))


reliable=[]
reliable2=[]
for i in range(39):
    reliable.append(np.sqrt(4/(data_num[i]-2+4)))
    reliable2.append(-np.sqrt(4/(data_num[i]-2+4)))
##################################################################


plt.figure(figsize=(10,5))
marker=['o','x','s','>','^','v','*','<','3','1']
legend=['p=0','p=1','p=2','p=3','p=4','p=5','p=6','p=7','p=8','p=9']
color=['red','maroon','pink', 'orange', 'olive', 'chartreuse', 'aqua','navy','darkcyan','grey']
ax=plt.subplot(111)

for x in range(len(code)):
    plt.plot(year,pcc[x], marker=marker[x], label=legend[x], color=color[x], lw=3)
plt.legend(loc='center left',  bbox_to_anchor=(1,0.65),frameon=False)


ax.fill_between(year,reliable,reliable2, facecolor='grey', alpha=0.2)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks( fontsize = 15)
plt.yticks( fontsize = 15)

plt.xlabel('t(year)', size='20')
plt.ylabel('$\\rho$({$\phi_p$(c,t)},{g(c,t)})', size='20')

plt.gcf().subplots_adjust(bottom=0.11, right=0.83)


plt.xlim([1962,2000])
#plt.savefig('evol_pcc.pdf', format='pdf', dpi=1000)
