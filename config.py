import configparser
from pathlib import Path
import pathlib
import os

class Config:

    def __init__(self):
        global config
        try:
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "config.conf"
            abs_file_path = os.path.join(script_dir, rel_path)
            configFile = Path(abs_file_path)
            assert os.path.exists(abs_file_path)
            print(configFile)
            config = configparser.ConfigParser()
            print('name ' + configFile.name)
            config.read(configFile.name)

            print(config.sections())
            mqttConfig = config['mqtt']
            d = dict(mqttConfig)
            print(d)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        

    def reloadFile():
        try:
            configFile = Path("./config.conf")
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        config = configparser.ConfigParser()
        config.read(configFile.name)
        
        

    def getConfigTopic(self):
        topic = config['mqtt']['topic']
        return topic

    def getConfigPort(self):
        port = config['mqtt']['port']
        return port

    def getConfigServerMqtt(self):
        serverMqtt = config['mqtt']['mqtt_server']
        return serverMqtt

    def getConfigMqtt(self):
        try:
            mqttConfig = config['mqtt']
            return dict(mqttConfig)
        except KeyError:
            print("Errore file configurazione")
            return ''
        

    def getConfigDevice(self):
        data = {}
        try:
            deviceConfig = config['device']['list']
            l = deviceConfig.split(',')
            for a in l:
                l = a.split(':')
                data[l[1]] = l[0]
            return data
        except KeyError:
            print("Errore file configurazione Device")
            return data
    
    def getTimeNoData(self):
        timeNoData = config['alert']['time_no_data']
        return timeNoData
    
    def getMinTemp(self):
        deviceConfig = config['alert']['minTemp']
        data = {}
        l = deviceConfig.split(',')
        for a in l:
            l = a.split(':')
            data[l[1]] = l[0]
        return data
    
    def getMaxTemp(self):
        data = {}
        try:
            deviceConfig = config['alert']['maxTemp']
            l = deviceConfig.split(',')
            for a in l:
                l = a.split(':')
                data[l[1]] = l[0]
            return data
        except KeyError:
            print("Errore file alert maxtremp")
            return data
    
    def getConfigUpdate(self):
        updateConfig = config['update']
        return updateConfig