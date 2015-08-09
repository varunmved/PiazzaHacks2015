import nltk
import redis
import urllib3
import requests
from firebase import firebase
from datetime import datetime
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from collections import Counter
import collections
from stemming.porter2 import stem
s=set(stopwords.words('english'))

requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://smartpoll.firebaseio.com/', None)
r = redis.StrictRedis(host='localhost', port=6379, db=0)


# def decideThumbs(Question,voteVal):
#     if voteVal > 0 :
#         ThumbsUp=1
#         putIntoFirebaseQuestionVote(Question,ThumbsUp)
#     else:
#         ThumbsDown=-1
#         putIntoFirebaseQuestionVote(Question,ThumbsDown)



#method for putting in a new question
def putIntoFirebaseNoUserQuestion(simpleQ):
    res = firebase.post('/BaseQuestion', simpleQ)

def putIntoFirebaseQuestion(Question):
    #result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
    print(Question)
    res = firebase.post('/Question',str(Question))
    #res = str(res[1])
    uniqID = res.get('name')
    #print("hi" + res)

    return uniqID

#method for putting in a thumbs up
def putIntoFirebaseQuestionVote(Question, ThumbsUp):
    res = ""
    res = '/' + Question +'/Vote'
    print(res)

    firebase.put(res,"voteVal",ThumbsUp)

#method to add an answer to an existing question
def putIntoFirebaseAnswerQuestion(Question,ID,Answer):
    res = ""
    #res = '/' + Question +'/'+ ID+'/Vote'
    res = "Question" + '/'+ ID;
    print(res)
    firebase.put(res,"Answer",Answer)

#method for putting in a thumbs down
def putIntoFirebaseQuestionVote(Question, ThumbsDown):
    res = ""
    res = '/' + Question +"/Vote"
    print(res)
    firebase.put(res,"voteVal",ThumbsDown)

def redisInit(id,Question):
    r.set(id,Question)
    #res = r.get('Question')
    #print(res)

def getFirebaseForNLTK():
    print("ayylmao")



def applyNLTK(strIn):
    res4= filter(lambda w: not w in s,strIn.split())
    sumStr = res1+res2+res3+res4
    sumStr2 = []
    for var in sumStr:
        var = stem(var)
        sumStr2.append(var)

    counter = collections.Counter(sumStr2)
    print(sumStr2)
    print(counter.most_common())


b1 = "hellooooo"
b2 = "What was Truman's foreign policy?"
b3 = "Who was Harry Truman's wife"
b4 = "When did George Washington get innaguarated?"
b5 = "Did George Washington want to be president?"


putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)
putIntoFirebaseNoUserQuestion(b1)

q1 = "Why am I cool?"
q2 = "Slayy lmao?"

ans1 = "2+2 = 4"
ans2 = "2+3 = 5"


idout1 =putIntoFirebaseQuestion(q1)
putIntoFirebaseAnswerQuestion(q1,idout1,ans1)
redisInit(idout1,q1)

#redisInit()



#decideThumbs(str1,1)
#decideThumbs(str1,2)
#decideThumbs(str2,-2)
