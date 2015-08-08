# Util class for Firebase
import requests
import json
import urllib3
import urllib
from firebase import firebase

requests.packages.urllib3.disable_warnings()

firebase = firebase.FirebaseApplication('https://smartpoll.firebaseio.com/', None)

#method for putting in a new question
def putIntoFirebaseQuestion(Question):
    firebase.put('/Question',"Question Title",Question)

# def putIntoFirebaseQuestionVote(VoteVal):
#     firebase.put('/')
#
# # methods for uber detection
# def putIntoFirebaseUber(GPS_Latitude, GPS_Longitude):
#     firebase.put('/Uber', "GPS_Start_Latitude", GPS_Latitude)  # Add data to Node Node1
#     firebase.put('/Uber', "GPS_Start_Longitude", GPS_Longitude)  # Add data to Node Node1
#     firebase.put('/Uber', "GPS_End_Latitude", GPS_Latitude - 1)  # Add data to Node Node1
#     firebase.put('/Uber', "GPS_End_Longitude", GPS_Longitude + 1)  # Add data to Node Node1
#
#
# # put into car methods
# def putIntoFirebaseCarBattery_Level(Battery_Level):
#     firebase.put('/Car', "Battery_Level", Battery_Level)
#
#
# def putIntoFirebaseCarHonk_State(Honk_State):
#     firebase.put('/Car', "Honk_State", Honk_State)
#
#
# def putIntoFirebaseCarFuel_Consumption(Fuel_Consumption):
#     firebase.put('/Car', "Fuel_Consumption", Fuel_Consumption)
#
#
# def putIntoFirebaseCarAccelerator_Pedal(Accelerator_Pedal):
#     firebase.put('/Car', "Accelerator_Pedal", Accelerator_Pedal)
#
#
# def putIntoFirebaseCarInside_Temperature(Inside_Temperature):
#     firebase.put('/Car', "Inside_Temperature", Inside_Temperature)
#
#
# def putIntoFirebaseCarFuel_Level(Fuel_Level):
#     firebase.put('/Car', "Fuel_Level", Fuel_Level)
#
#
# def putIntoFirebaseCarTire_Pressure_Front_Left(Tire_Pressure_Front_Left):
#     firebase.put('/Car', "Tire_Pressure_Front_Left", Tire_Pressure_Front_Left)
#
#
# def putIntoFirebaseCarOutside_Air_Temperature(Outside_Air_Temperature):
#     firebase.put('/Car', "Outside_Air_Temperature", Outside_Air_Temperature)
#
#
# def putIntoFirebaseCarOdometer(Odometer):
#     firebase.put('/Car', "Odometer", Odometer)
#
#
# def putIntoFirebaseCarDoor_State_Front_Right(Door_State_Front_Right):
#     firebase.put('/Car', "Door_State_Front_Right", Door_State_Front_Right)
#
#
# def putIntoFirebaseCarTire_Pressure_Rear_Left(Tire_Pressure_Rear_Left):
#     firebase.put('/Car', "Tire_Pressure_Rear_Left", Tire_Pressure_Rear_Left)
#
#
# def putIntoFirebaseCarTire_Pressure_Front_Right(Tire_Pressure_Front_Right):
#     firebase.put('/Car', "Tire_Pressure_Front_Right", Tire_Pressure_Front_Right)
#
#
# def putIntoFirebaseCarTire_Pressure_Rear_Right(Tire_Pressure_Rear_Right):
#     firebase.put('/Car', "Tire_Pressure_Rear_Right", Tire_Pressure_Rear_Right)
#
#
# def putIntoFirebaseCarTimestamp(Timestamp):
#     firebase.put('/Car', "Timestamp", Timestamp)
#
#
# def putIntoFirebaseCarDoor_State_Rear_Left(Door_State_Rear_Left):
#     firebase.put('/Car', "Door_State_Rear_Left", Door_State_Rear_Left)
#
#
# def putIntoFirebaseCarFuel_Level_Critical(Fuel_Level_Critical):
#     firebase.put('/Car', "Fuel_Level_Critical", Fuel_Level_Critical)
#
#
# def putIntoFirebaseCarDoor_State_Rear_Right(Door_State_Rear_Right):
#     firebase.put('/Car', "Door_State_Rear_Right", Door_State_Rear_Right)
#
#
# def putIntoFirebaseCarVehicle_Speed(Vehicle_Speed):
#     firebase.put('/Car', "Vehicle_Speed", Vehicle_Speed)
#
#
# def putIntoFirebaseCarDoor_State_Front_Left(Door_State_Front_Left):
#     firebase.put('/Car', "Door_State_Front_Left", Door_State_Front_Left)
#
#
# def putIntoFirebaseCarIgnition_State(Ignition_State):
#     firebase.put('/Car', "Turn_Indicator_State", Ignition_State)
#
#
# def putIntoFirebaseCarTurn_Indicator_State(Turn_Indicator_State):
#     firebase.put('/Car', "Turn_Indicator_State", Turn_Indicator_State)
#
#
# def putIntoFirebaseSpeedLimit(speedLimit_value, speedLimit_unit):
#     firebase.put('/Car', "SpeedLimit_Value", speedLimit_value)
#     firebase.put('/Car', "SpeedLimit_Unit", speedLimit_unit)
#
#
# def putIntoFirebaseUberTimes(data):
#     for i in data['times']:
#         firebase.put('/Uber/Times', i['localized_display_name'], i['estimate'])
#
#
# def putIntoFirebaseUberPrice(data):
#     for i in data['prices']:
#         print i['localized_display_name']
#         print i['distance']
#         firebase.put('/Uber/Prices/Low', i['localized_display_name'], i['low_estimate'])
#         firebase.put('/Uber/Prices/High', i['localized_display_name'], i['high_estimate'])
#
#
# def putIntoFirebaseTwilio(name, toNumber, currTime):
#     firebase.put('/Twilio', 'callPlaced', 'yes')
#     firebase.put('/Twilio', 'name', name)
#     firebase.put('/Twilio', 'number', toNumber)
#     firebase.put('/Twilio', 'time', currTime)
#
#
# def putIntoFirebaseUberState(state):
#     firebase.put('/Uber', "drunk", state)
