from nltk.corpus import stopwords
from nltk.tag import pos_tag
from collections import Counter
import collections
from stemming.porter2 import stem
s=set(stopwords.words('english'))

b1 = "hellooooo"
b2 = "What was Truman's foreign policy?"
b3 = "Who was Harry Truman's wife"
b4 = "When did George Washington get innaguarated?"
b5 = "Did George Washington want to be president?"


b8 = "what's a pointer"
b6 = "how do i allocate a pointer"
b9 = "I allocated a pointer"

b7 = "what does freeing a pointer do"



# print filter(lambda w: not w in s,b2.split())
#
# print filter(lambda w: not w in s,b3.split())
#
# print filter(lambda w: not w in s,b4.split())
# print filter(lambda w: not w in s,b5.split())

res1= filter(lambda w: not w in s,b8.split())
res2= filter(lambda w: not w in s,b6.split())
res3= filter(lambda w: not w in s,b7.split())
res4= filter(lambda w: not w in s,b9.split())



sumStr = res1+res2+res3+res4
sumStr2 = []
for var in sumStr:
    var = stem(var)
    sumStr2.append(var)

counter = collections.Counter(sumStr2)
print(sumStr2)
print(counter.most_common())
