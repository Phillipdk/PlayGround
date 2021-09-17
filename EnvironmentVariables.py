""" 
This test is to test the API call and see if it works. It is an 
integration test.
"""
import os

TemperatureVector = [120, 110, 130, 150] # Temperture [celsius]
TimeVectorHr =      [0,   1,   2,   3  ] # Time [Hr]

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
componentId = os.environ['COMPONENT_ID']


print(client_id)
print(client_secret)
print(componentId)