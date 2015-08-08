import nltk
import redis
import urllib3
import requests
from firebase import firebase
from datetime import datetime

requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://smartpoll.firebaseio.com/', None)

def decideThumbs(voteVal):
    if voteVal > 0 :
        ThumbsUp=1
        putIntoFirebaseQuestionVote(ThumbsUp)
    else:
        ThumbsDown=-1
        putIntoFirebaseQuestionVote(ThumbsDown)


#method for putting in a new question
def putIntoFirebaseQuestion1():
    here = "here"
    firebase.put('/Question',"Question Title", here)

def putIntoFirebaseQuestion(Question):
    #result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})

    firebase.post('/Question',"Question Title",Question)

#method for putting in a thumbs up
def putIntoFirebaseQuestionVote(Question, ThumbsUp):
    # try:
    #     firebase.get('/Question/Vote',"voteVal",ThumbsUp)

    firebase.put('/Question/Vote',"voteVal",ThumbsUp)



#method for putting in a thumbs down
def putIntoFirebaseQuestionVote(ThumbsDown):
    firebase.put('/Question/Vote',"voteVal",ThumbsDown)


putIntoFirebaseQuestion1()
putIntoFirebaseQuestion("Why am I cool?")
putIntoFirebaseQuestion("Slayy lmao?")

decideThumbs(1)
decideThumbs(2)
decideThumbs(-2)
