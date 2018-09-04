#Progetto   client mqtt con python per interfaccia raspberry

import paho.mqtt.client as mqtt
from config import Config
import Queue, time, json
from datetime import datetime
from time import strftime

class Mqtt:

    def __init__(self,  queue, con):
        global configMqtt, configuration
        self.q = queue
        configuration = con
        configMqtt = configuration.getConfigMqtt()


    def on_message(self,client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        jsondata = json.loads(msg)
        t = time.ctime(time.time())
        jsondata['localtime'] = str(t)#strftime("%a, %d %b %Y %H:%M:%S +0000", t)
        #str(t)
        print 'inserito msg ' + json.dumps(jsondata)
        self.q.put(jsondata)
    
    def on_connect(self,client, userdata,flags, rc):
        print("Connected with result code "+str(rc))
        topic = configMqtt['topic']
        clientMqtt.subscribe(topic)

    def connect(self):
        global clientMqtt 
        print "configMqtt: " + str(configMqtt)
        clientId = 'bolsezanadisplay'
        port = configMqtt['port']
        mqttServer = configMqtt['mqtt_server']
        username = configMqtt['username']
        password = configMqtt['password']
        clientMqtt = mqtt.Client(clientId)
        clientMqtt.on_connect = self.on_connect
        clientMqtt.on_message = self.on_message
        clientMqtt.username_pw_set(username,password)
        clientMqtt.connect(mqttServer,str(port),60,'')
        while True:
            time.sleep(2)
            clientMqtt.loop(timeout=1.0, max_packets=6)
        #clientMqtt.loop_forever()
        #clientMqtt.loop(0.01)


