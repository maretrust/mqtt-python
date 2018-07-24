from config import Config
import urllib2


class Update:

    def __init__(self):
        global config,configUpdate
        configuration = Config()
        configUpdate = configuration.getConfigUpdate()

    def getConfigFile(self):
        try:
            address = configUpdate["server"]+":"+ configUpdate["port"]+configUpdate["folder"]+configUpdate["file"]
            contentsFileConfig = urllib2.urlopen(address).read()
            configFile = open("config.conf", "w")
            configFile.write(contentsFileConfig)
            configFile.close()  
            print "file aggiornato"
        except urllib2.HTTPError:
            print "file non ce"
        
        