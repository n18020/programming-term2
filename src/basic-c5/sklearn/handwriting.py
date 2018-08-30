from sklearn import datasets, cross_validation, svm, metrics

digits = datasets.load_digits()
data_train, data_test, label1_train, label_test = \
    cross_validation.train_test_split(digits.data, digits.target)

clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label1_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label1_test, predict)
print('分類機の情報=', clf)
print('正解率=', ac_score)
print('レポート=\n', cl_report)
