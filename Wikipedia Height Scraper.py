import csv
import re
heighttext = []
trees = []

with open('\stree-heighttext.csv') as csvfileDSM:
    readerDSM = csv.reader(csvfileDSM, delimiter=',')
    for row in readerDSM:
        heighttext.append(row[1])
        trees.append(row[0])

# for i in heighttext[:4]:
#     print(i)

import re

def search(target, text, context=4):
    # It's easier to use re.findall to split the string,
    # as we get rid of the punctuation
    words = re.findall(r'\w+', text)

    matches = (i for (i,w) in enumerate(words) if w.lower() == target)
    for index in matches:
        if index < context //2:
            yield words[0:context+1]
        elif index > len(words) - context//2 - 1:
            yield words[-(context+1):]
        else:
            yield words[index - context//2:index + context//2 - 1]

print(len(heighttext))
newlist = []
for i in heighttext:
    s = list(search('m', i))
    if (len(s) > 0):
        j = ' '.join(s[0])
        k = re.findall('\d+', j)
        if (len(k) != 0):
            k = [int(i) for i in k]
            l = sum(k)/len(k)
            newlist.append(l)
    else:
        s = list(search('meters', i))
        if (len(s) > 0):
            j = ' '.join(s[0])
            k = re.findall('\d+', j)
            if (len(k) != 0):
                k = [int(i) for i in k]
                l = sum(k)/len(k)
                newlist.append(l)
        else:
                s = list(search('metres', i))
                if (len(s) > 0):
                    j = ' '.join(s[0])
                    k = re.findall('\d+', j)
                    if (len(k) != 0):
                        k = [int(i) for i in k]
                        l = sum(k)/len(k)
                        newlist.append(l)
                else:
                    newlist.append("none")

combine = [[a, b, c]for a, b, c in zip(trees, newlist, heighttext)]


with open('\stree-avg-heighttext.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(combine)
