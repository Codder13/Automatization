from configparser import ConfigParser

config1 = ConfigParser()
config1['saved_paths'] = {
    'value1': 'ok',
    'value2': '2',
    'value3': '4'
}

dict = dict(config1.items('saved_paths'))
values_list = [v for k, v in dict.items()]
print(values_list)
