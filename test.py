import configparser,os, pathlib
from pathlib import Path

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "config.conf"
abs_file_path = os.path.join(script_dir, rel_path)
configFile = Path(abs_file_path)
assert os.path.exists(abs_file_path)
print configFile
config = configparser.RawConfigParser()
print 'name ' + configFile.name
config.read(configFile.name)

print config.sections()
mqttConfig = config['mqtt']
d = dict(mqttConfig)
print d



