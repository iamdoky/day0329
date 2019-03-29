from sklearn import svm,metrics
import re
import random

#  csv 파일 읽어오기
csv = []
with open('iris.csv','r',encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        fn = lambda n: float(n) if re.match('^[0-9\.]+$',n) else n
        # cols = list(map(fn,cols))
        # csv.append(cols)
        rList = []
        for c in cols:
            temp = fn(c)
            rList.append(temp)
        csv.append(rList)

# 헤더를 삭제
del csv[0]

# csv를 섞는다.
random.shuffle(csv)

# 데이터 분활
total_len = len(csv)
train_len = int(total_len * 2/3)

train_data = []
train_lavbel = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:4]
    lavel = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_lavbel.append(lavel)
    else:
        test_data.append(data)
        test_label.append(lavel)

# 학습하고 예측
clf = svm.SVC()
clf.fit(train_data,train_lavbel)

pre = clf.predict(test_data)

# 정답을 구하자
score = metrics.accuracy_score(test_label,pre)
print('정답률: ',score)


# realData = [[6.0,2.2,4.0,1.0]]
# result = clf.predict(realData)
# print(result)
