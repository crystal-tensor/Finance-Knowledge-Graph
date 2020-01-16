# -*- coding: utf-8 -*-
# coding: utf-8
import numpy as np
import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

#csv_file = 'data1.csv'
csv_file = 'news20200103_2.csv'
f = open(csv_file, 'r', encoding="gbk", errors='ignore')   ##encoding=u'utf-8', encoding='gbk'
#f = open(csv_file, 'r', encoding="ISO-8859-1", errors='ignore')
data = pd.read_csv(f)
data.head()
#t=pd.DataFrame(data['comment'].astype(str))
#print(t)
#data = pd.read_csv('news20200103_2.csv',encoding="unicode_escape")

#print(data.head())
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))
data['cut_comment'] = data.comment.apply(chinese_word_cut)
X = data['cut_comment']
print(X)
y = data.sentiment

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords = f.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list

stop_words_file = '哈工大停用词表.txt'

stopwords = get_custom_stopwords(stop_words_file)

vect = CountVectorizer(max_df = 0.8,
                       min_df = 3,
                       token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
                       stop_words=frozenset(stopwords))
#print(vect)
test = pd.DataFrame(vect.fit_transform(X_train).toarray(), columns=vect.get_feature_names())
test.head()

nb = MultinomialNB()

X_train_vect = vect.fit_transform(X_train)

nb.fit(X_train_vect, y_train)
train_score = nb.score(X_train_vect, y_train)
print('准确率',train_score)

# X_test_vect = vect.transform(X_test)
# print(nb.score(X_test_vect, y_test))

X_vec = vect.transform(X)
nb_result = nb.predict(X_vec)
data['nb_result'] = nb_result


