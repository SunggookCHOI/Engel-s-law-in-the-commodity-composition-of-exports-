
g = open('Export_from_wtfname.txt','r')

countryNm = []
countryCd = []

lines2=g.read().split('\n')
lines2.pop()
for line in lines2:
    b=line.split('\t')
    if len(b)==2 and b[0] not in countryNm:
        countryNm.append(b[0])
        countryCd.append(b[1])
g.close()

products=[str(x) for x in range(10)]
year=[x for x in range(1962,2001)]

f = open('rgdp_DSL.ver1.txt','r')
lines3 = f.read().split('\n')
lines3.pop()
f.close()

gCountry=[[] for i in year]
gdp=[[] for i in year]



for line in lines3:
    b=line.split('\t')
    if int(b[2]) in year and b[1] not in gCountry[year.index(int(b[2]))] and b[1] in countryCd:
        gCountry[year.index(int(b[2]))].append(b[1])
        gdp[year.index(int(b[2]))].append(float(b[3]))

for i in range(len(gdp)):
    tempSum = sum(gdp[i])
    gdp[i] = [x/tempSum for x in gdp[i]]


finalCountry=[[] for i in year]
port = [[] for i in year]

f = open('Export_from_wtf.txt','r')
lines=f.read().split('\n')
lines.pop()
f.close()
iii=0
for line in lines:
    b=line.split('\t')
    if int(b[0]) in year and b[2] != 'World' and b[2] in countryNm:
        tempCd = countryCd[countryNm.index(b[2])]
        yearIndex = year.index(int(b[0]))
        if tempCd in gCountry[yearIndex] :
            if tempCd in finalCountry[yearIndex] :
                port[yearIndex][finalCountry[yearIndex].index(tempCd)][products.index(b[3][0])+3] += float(b[4])
            else :
                finalCountry[yearIndex].append(tempCd)
                tList=[b[0],tempCd, gdp[yearIndex][gCountry[yearIndex].index(tempCd)]]
                for i in range(len(products)):
                    tList.append(0)
                tList[products.index(b[3][0])+3] += float(b[4])
                port[yearIndex].append(tList)
    if iii%50000==0:
        print(iii/len(lines))
    iii+=1
    
for i in range(len(port)):
    for j in range(len(port[i])):
        tempSum = sum(port[i][j][3:])
        for k in range(3,len(port[i][j])):
            port[i][j][k] = port[i][j][k]/tempSum
    
f = open('port_onedigit.txt','w')
for i in range(len(port)):
    for j in range(len(port[i])):
        f.write(port[i][j][0]+'\t'+port[i][j][1]+'\t'+str(port[i][j][2]))
        for k in range(3,len(port[i][j])):       
            f.write('\t'+str(port[i][j][k]))
        f.write('\n')
f.close()        
        
        
        
        
        
        