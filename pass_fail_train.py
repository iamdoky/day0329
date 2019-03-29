from sklearn import svm, metrics
data = [
    [20,100,'합격'],
    [18,3,'불합격'],
    [15,10,'불합격'],
    [18,80,'합격'],
    [18,0,'불합격'],
    [20,90,'합격'],
    [20,100,'합격'],
    [17,50,'불합격'],
    [19,90,'합격'],
    [14,50,'불합격']
]
data2 = data[:7]
data3 = data[7:]

d2 = []
l2 = []
d3 = []
l3 = []

for i in range(len(data2)):
    row = data2[i]
    days = row[0]
    hours = row[1]
    isPass = row[2]
    d2.append([days,hours])
    l2.append(isPass)

for i in range(len(data3)):
    row = data3[i]
    days = row[0]
    hours = row[1]
    isPass = row[2]
    d3.append([days,hours])
    l3.append(isPass)

clf = svm.SVC()
clf.fit(d2,l2)

r = clf.predict(d3)

acc= metrics.accuracy_score(l3,r)
print(acc)

