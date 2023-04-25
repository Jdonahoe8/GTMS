import time
import paho.mqtt.client as paho

#broker="broker.hivemq.com"
broker="169.254.160.223"
#broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

    
myDict = {'Coolant_Temperature' : 0, 'ECU_Battery_Voltage' : 0, 'Engine_Oil_Pressure' : 0, 'Engine_Oil_Temperature' : 0,'Engine_Speed' : 0, 'ABSMAP_raw' : 0, 'Vehicle_Speed' : 0,'Exhaust_Lambda' : 0, 'Fuel_Pressure_Sensor' : 0, 'Gear' : 'N','Wheel_Speed_FL': 0, 'Wheel_Speed_FR' : 0,'Wheel_Speed_RL' : 0, 'Wheel_Speed_RR' : 0,'Throttle_Position' : 0, 'Engine_State' : 0, 'Fuel_Pump_State' : 0,'Brake_Temp_FL' : 0, 'Brake_Temp_FR' : 0, 'Brake_Temp_RL' : 0,'Brake_Temp_RR' : 0}               
print(str(myDict))

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("GTMS/telemetry")#subscribe
time.sleep(2)
print("publishing ")
client.publish("GTMS/telemetry",str(myDict))#publish
i = 0
while (True):
    time.sleep(8)
    myDict['Coolant_Temperature'] += 1
    client.publish("GTMS/telemetry",str(myDict))
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
