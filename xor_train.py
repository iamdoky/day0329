from sklearn import svm

xor_data = [

#   [변수, 변수(문제), 라벨(정답)] / 계산 결과 데이터
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
#   학습을 위한 데이터와 레이블 분리
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)

#   데이터 학습.
clf = svm.SVC()
clf.fit(data,label)

#   데이터 예측.
pre = clf.predict(data)
print("예측결과: ",pre)

#   결과 확인.
ok = 0
total = len(label)
for i in range(len(label)):
    answer = label[i]
    p = pre[i]
    if answer == p:
        ok = ok+1

# ok = 0; total = 0
# for idx, answer in enumerate(label):
#     p = pre[idx]
#     if p == answer:
#         ok += 1
#     total += 1
print("정답률:",ok,"/",total,"=",ok/total)
