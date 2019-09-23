import matplotlib.pyplot as plt
import cartopy
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs

t1=['LEB','KUW','SAU','IRQ','LIB','VEN','IRN','TRI','OMA']
t2=['BUL','TAW','POL','CAO','EQG','DEN','IRE','SPN','MAG','ARG','SRI','GUA','MYA','TOG','SAL','HON','HAI','CAM','BRA','GHA','CDI','ETH','UGA','COL','CUB','ECU','COS','ICE','DOM','SOM','BFO']
t3=['DRC','CHL','AUS','JPN','BEL','HUN','YUG','POR','NOR','ISR','IND','CHN','FIN','CAN','PRK','PAN','SWD','GDR','NTH','ITA','FRN','CZE','USA','GFR','UKG']
t4=['MON','CHA','BOL','NIR','SUD','BUI','BEN','LBR','JOR','NEP','PAK','URU','AFG','SIE','MAL','CON','GAB']
t5=['TUR','GRC','SEN','JAM','PHI','MLI','TAZ','NIC','PAR','PER','SAF','CEN','MEX','ROK','MOR','AUL','MAA','CYP','THI','NEW','EGY','NIG','INS','ALB','SYR','TUN','RUM','RUS']
etc=['GUI','ALG']
g1962=[t1,t2,t3,t4,t5,etc]

tt1=['IRQ','LIB','KUW','ALG','NIG','OMA','IRN','SAU','GAB','SUD','SYR','EQG','CON','VEN','NOR','NIR','TRI']
tt2=['ECU','CAO','DRC','RUS','EGY','COL']
tt3=['MON','TOG','AFG','MLI','GUI','BEN','BFO','PAR','JAM','CHA']
tt4=['NEP','HAI','CAM','SAL','HON','DOM','SRI']
tt5=['ICE','URU','NEW','GHA','TAZ','CHL','PER','ARG','BOL','AUL','SEN','UGA','ETH','CDI','BUI','SOM','MAA','CUB']
tt6=['BRA','COS','PAN','DEN','SPN','CYP','THI','SWD','GFR','FRN','UKG','SIE','MEX','ROK','TAW','USA','HUN','CAN','PRK','NTH','BEL','POL','ITA','POR','FIN','ISR','AUS','LBR','PHI','JPN','MAL']
tt7=['TUN','CHN','MOR','MYA','SAF','PAK','IND','YUG','INS','GRC','BUL','ALB','RUM','LEB','TUR']
etc2=['GUA','MAG','NIC','CEN','JOR','IRE']
g2000=[tt1,tt2,tt3,tt4,tt5,tt6,tt7,etc2]


year=1962

f=open('/home/choi/work/python/world/countrycode/CountryCodeMapping.rev2.txt','r')
lines=f.read().split('\n')

matching=[[],[]]
for line in lines:
    x=line.split('\t')
    for i in range(len(x)):
        matching[i].append(x[i])


g1962a=[[] for i in range(len(g1962))]
g2000a=[[] for i in range(len(g2000))]

for i in range(len(g1962)):
    for j in range(len(g1962[i])):
        if g1962[i][j] in matching[0]:
            g1962a[i].append(matching[1][matching[0].index(g1962[i][j])])
        if g1962[i][j] in matching[1]:
            g1962a[i].append(matching[0][matching[1].index(g1962[i][j])])

for i in range(len(g2000)):
    for j in range(len(g2000[i])):
        if g2000[i][j] in matching[0]:
            g2000a[i].append(matching[1][matching[0].index(g2000[i][j])])
        if g2000[i][j] in matching[1]:
            g2000a[i].append(matching[0][matching[1].index(g2000[i][j])])



fig=plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.OCEAN)
ax.set_extent([-150, 60, -25, 60])

shpfilename = shpreader.natural_earth(resolution='110m',
                                      category='cultural',
                                      name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

g20002=[]
g20002a=[]
for x in g2000:
    g20002.extend(x)
for x in g2000a:
    g20002a.extend(x)

all_exist=g20002+g20002a

target=g2000
target2=g2000a
c=['r','g','b','skyblue','purple','yellow','k','orange']

ass=[]
for country in countries:
    if country.attributes['ADM0_A3'] == 'SAH':
        print(country)
    
    for i in range(len(target)):
        if country.attributes['ADM0_A3'] in target[i] or country.attributes['ADM0_A3'] in target2[i]:
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                          facecolor=c[i],
                          label=country.attributes['ADM0_A3'])
    if country.attributes['ADM0_A3'] not in all_exist:
        print(country.attributes['ADM0_A3'])
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                          facecolor='grey',
                          label=country.attributes['ADM0_A3'])
        
    ass.append(country.attributes['ADM0_A3'])

plt.title('2000')
plt.show()

fig=plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cartopy.feature.OCEAN)
ax.set_extent([-150, 60, -25, 60])

shpfilename = shpreader.natural_earth(resolution='110m',
                                      category='cultural',
                                      name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

target=g1962
target2=g1962a

g19622=[]
g19622a=[]
for x in g1962:
    g19622.extend(x)
for x in g1962a:
    g19622a.extend(x)
all_exist2=g19622+g19622a

for country in countries:
    for i in range(len(target)):
        if country.attributes['ADM0_A3'] in target[i] or country.attributes['ADM0_A3'] in target2[i]:
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                          facecolor=c[i],
                          label=country.attributes['ADM0_A3'])
    if country.attributes['ADM0_A3'] not in all_exist2:
        print(country.attributes['ADM0_A3'])
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                          facecolor='grey',
                          label=country.attributes['ADM0_A3'])
    ass.append(country.attributes['ADM0_A3'])
plt.title('1962')
plt.show()
