#f = open('C:/Users/최성국/Desktop/work/trade/data/portfolio5.txt','r')
f = open('../data/port_onedigit.txt','r')

lines=f.read().split('\n')
lines.pop()
#code=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '21', '22', '23', '24', '25', '26', '27', '28', '29', '32', '33', '34', '35', '41', '42', '43', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '87', '88', '89', '90', '91', '93', '94', '95', '96', '97', '0A', '0X', '1A', '1X', '2A', '2X', '3A', '3X', '4A', '4X', '5A', '5X', '6A', '6X', '7A', '7X', '8A', '8X', '9A', '9X']
code=['0','1','2','3','4','5','6','7','8','9']
c1=['LEB','KUW','SAU','IRQ','LIB','VEN','IRN','TRI','OMA']
c2=['BUL','TAW','POL','CAO','EQG','DEN','IRE','SPN','MAG','ARG','SRI','GUA','MYA','TOG','SAL','HON','HAI','CAM','BRA','GHA','CDI','ETH','UGA','COL','CUB','ECU','COS','ICE','DOM','SOM','BFO']
c3=['DRC','CHL','AUS','JPN','BEL','HUN','YUG','POR','NOR','ISR','IND','CHN','FIN','CAN','PRK']
c4=['PAN','SWD','GDR','NTH','ITA','FRN','CZE','USA','GFR','UKG']
c5=['MON','CHA','BOL','NIR','SUD','BUI','BEN','LBR','JOR','NEP','PAK','URU','AFG','SIE','MAL','CON','GAB']
c6=['TUR','GRC','SEN','JAM','PHI','MLI','TAZ','NIC','PAR','PER','SAF','CEN','MEX','ROK','MOR','AUL','MAA','CYP','THI','NEW']
c7=['EGY','NIG','INS','ALB','SYR','TUN','RUM','RUS']
print(len(c6))
etc=['GUI','ALG']

country=c1+c2+c3+c4+c5+c6+c7+etc


d1=['IRQ','LIB','KUW','ALG','NIG','OMA','IRN','SAU','GAB','SUD','SYR','EQG','CON','VEN','NOR','NIR','TRI']
d2=['ECU','CAO','DRC','RUS','EGY','COL']
d3=['MON','TOG','AFG','MLI','GUI','BEN','BFO','PAR','JAM','CHA']
d4=['GUA','MAG','NIC']
d5=['NEP','HAI','CAM','SAL','HON','DOM','SRI']
d6=['ICE','URU','NEW','GHA','TAZ','CHL','PER','ARG','BOL','AUL']
d7=['SEN','UGA','ETH','CDI','BUI','SOM','MAA','CUB']
d8=['BRA','COS','PAN','DEN','SPN','CYP','THI','SWD','GFR','FRN','UKG','SIE','MEX','ROK','TAW','USA','HUN','CAN','PRK','NTH','BEL','POL','ITA','POR','FIN','ISR','AUS','LBR','PHI','JPN','MAL']
d9=['TUN','CHN','MOR','MYA','SAF','PAK','IND','YUG','INS','GRC','BUL','ALB','RUM','LEB','TUR']
etc2=['CEN','JOR','IRE']

#######threshold=0.485#############
t1=['LEB','KUW','SAU','IRQ','LIB','VEN','IRN','TRI','OMA']
t2=['BUL','TAW','POL','CAO','EQG','DEN','IRE','SPN','MAG','ARG','SRI','GUA','MYA','TOG','SAL','HON','HAI','CAM','BRA','GHA','CDI','ETH','UGA','COL','CUB','ECU','COS','ICE','DOM','SOM','BFO']
t3=['DRC','CHL','AUS','JPN','BEL','HUN','YUG','POR','NOR','ISR','IND','CHN','FIN','CAN','PRK','PAN','SWD','GDR','NTH','ITA','FRN','CZE','USA','GFR','UKG']
t4=['MON','CHA','BOL','NIR','SUD','BUI','BEN','LBR','JOR','NEP','PAK','URU','AFG','SIE','MAL','CON','GAB','TUR','GRC','SEN','JAM','PHI','MLI','TAZ','NIC','PAR','PER','SAF','CEN','MEX','ROK','MOR','AUL','MAA','CYP','THI','NEW','EGY','NIG','INS','ALB','SYR','TUN','RUM','RUS']

tt1=['IRQ','LIB','KUW','ALG','NIG','OMA','IRN','SAU','GAB','SUD','SYR','EQG','CON','VEN','NOR','NIR','TRI']
tt2=['ECU','CAO','DRC','RUS','EGY','COL']
tt3=['MON','TOG','AFG','MLI','GUI','BEN','BFO','PAR','JAM','CHA']
tt4=['GUA','MAG','NIC','NEP','HAI','CAM','SAL','HON','DOM','SRI']
tt5=['ICE','URU','NEW','GHA','TAZ','CHL','PER','ARG','BOL','AUL','SEN','UGA','ETH','CDI','BUI','SOM','MAA','CUB']
tt6=['BRA','COS','PAN','DEN','SPN','CYP','THI','SWD','GFR','FRN','UKG','SIE','MEX','ROK','TAW','USA','HUN','CAN','PRK','NTH','BEL','POL','ITA','POR','FIN','ISR','AUS','LBR','PHI','JPN','MAL','TUN','CHN','MOR','MYA','SAF','PAK','IND','YUG','INS','GRC','BUL','ALB','RUM','LEB','TUR']
#############################################
country2=d1+d2+d3+d4+d5+d6+d7+d8+d9+etc2
print(len(country),len(country2))
for x in country:
    if x not in country2:
        print(x)


x=input('연도:')
a=[]
l=[]   #해당 국가
for each_line in lines:
    b=each_line.split()
    if b[0]==x and b[1] in country:           
        a.append(each_line)

c=[[] for x in range(len(a))]
for x in range(len(a)):
    b=a[x].split('\t')
    l.append(b[1])
    for j in range(len(code)):
        c[x].append(b[j+3])

print(len(c[0]),c[0])
print(len(c[1]),c[1])

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

Z=linkage(c,'average')
print(len(c))


fig=plt.figure(figsize=(2,9.3))
plt.xticks([])
dendrogram(
    Z,
    labels=l,
    distance_sort='descending',
    leaf_font_size=14., 
    orientation='right'

)
ax=plt.gca()
ax.tick_params(axis='y', which='major', labelsize=6)
plt.gcf().subplots_adjust(bottom=0.05, top=0.98, left=0.15)

plt.show()
#plt.savefig('dend2000.eps', format='eps', dpi=1000)