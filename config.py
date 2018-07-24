import configparser
from pathlib import Path
import pathlib

class Config:

    def __init__(self):
        global config
        try:
            configFile = Path("./config.conf")
            configFile.resolve()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        config = configparser.ConfigParser()
        config.read(configFile.name)
    
    def reloadFile(self):
        try:
            configFile = Path("./config.conf")
            configFile.resolve()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
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
            return mqttConfig
        except KeyError:
            print "Errore file configurazione"
            return ''
        

    def getConfigDevice(self):
        data = {}
        try:
            deviceConfig = config['device']['list']
            l = deviceConfig.split(',')
            for a in l:
                l = a.split(':')
                data[l[1]]=l[0]
            return data
        except KeyError:
            print "Errore file configurazione Device"
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
            data[l[1]]=l[0]
        return data
    
    def getMaxTemp(self):
        deviceConfig = config['alert']['maxTemp']
        data = {}
        l = deviceConfig.split(',')
        for a in l:
            l = a.split(':')
            data[l[1]]=l[0]
        return data
    
    def getConfigUpdate(self):
        updateConfig = config['update']
        return updateConfig