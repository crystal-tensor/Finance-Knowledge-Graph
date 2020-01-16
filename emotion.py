
from snownlp import SnowNLP


text2 = '2019年拉美地区经济增速放缓'
text1 = '大数据“杀熟”？ 鲜花包月质量忽上忽下的原因终于找到了,减薪裁员、旅客锐减……港媒：香港为春节经济忧愁'

s1 = SnowNLP(text1)
s2 = SnowNLP(text2)

print(s1.sentiments,s2.sentiments)