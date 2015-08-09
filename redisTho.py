import redis
from firebase import firebase
import urllib3
import requests

firebase1 = firebase.FirebaseApplication('https://redistrial.firebaseio.com/', None)
firebase2 = firebase.FirebaseApplication('https://redistrial.firebaseio.com/', None)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def redisInit():
    res = ""
    while res != None:
        res = firebase1.get('/Question',)
        print(res)
        r.set("name",res)
    #pipe = r.pipeline()
    # r.rpush('name','varun')
    # r.rpush('name','aniket')
    # r.rpush('name','cgslayer')


def letsGetDatData():
    # while True:
    #     #run forever
    #     for redisData in r.keys():
    #         print(r.keys('name'))
    #         redisGet = r.get('name')
    #         firebase.put('/Res',"voteVal",redisGet)

    # while r.keys() != True:
    #     print(r.keys('name'))
    #     redisGet = r.get('name')
    #     firebase.post('/Res',redisGet)

    for key in r.scan_iter():
        redisGet = r.get('')
        firebase2.post('/Res',redisGet)

redisInit()
letsGetDatData()
