import csv

heighttext = []
heights = []
trees = []
dsmheights = []
tree_c = []
newlist = []
diameters = []

with open('\stree-avg-heighttext.csv') as csvfileDSM:
    readerDSM = csv.reader(csvfileDSM, delimiter=',')
    for row in readerDSM:
        heights.append(row[1])
        heighttext.append(row[2])
        trees.append(row[0])

with open('\sfinal-country-species-diameter-height-type.csv') as csvfileDSM:
    readerDSM = csv.reader(csvfileDSM, delimiter=',')
    for row in readerDSM:
        d = []
        d.append(row[0])
        d.append(row[1])
        d.append(row[2])
        d.append(row[5])
        diameters.append(row[8])
        newlist.append(d)
        dsmheights.append(row[6])
        tree_c.append(row[2])

conifers = ['Pinaceae', 'Podocarpaceae', 'Cupressaceae', 'Araucariaceae', 'Cephalotaxaceae', 'Phyllocladaceae', 'Sciadopityaceae', 'Taxaceae']

counter = 0
for i in tree_c:
    if i in trees:
        for j in trees:
            if (i == j):
                ind = trees.index(j)
                if (dsmheights[ind] != ''):
                    newlist[counter].append(dsmheights[ind])
                elif (heights[ind] != 'none'):
                    newlist[counter].append(heights[ind])
                else:
                    newlist[counter].append(-999)
    else:
        newlist[counter].append(-111)

    if (float(newlist[counter][4]) > 6):
        newlist[counter][3] = 'Tree'
    if newlist[counter][1] in conifers:
        newlist[counter][3] = 'Conifer'
    if newlist[counter][1] == 'Arecaceae':
        newlist[counter][3] = 'Palm'
    counter += 1


dia = []
for i in diameters:
    if i:
        dia.append(i)


listwithlabels = []
for i in newlist:
    if (i[3] != '-'):
        listwithlabels.append(i)

print(len(newlist))
print(len(listwithlabels))

listalldata = []
for i in listwithlabels:
    if (float(i[4]) > 0):
        listalldata.append(i)

print(len(listalldata))
duptrees = []
for i in listalldata:
    duptrees.append(i[2])

finallist = []
with open('\Finaldata2.csv') as csvfileDSM:
    readerDSM = csv.reader(csvfileDSM, delimiter=',')
    for row in readerDSM:
        if (float(row[4]) > 0):
            finallist.append(row)

with open('\Finaldata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(finallist)
