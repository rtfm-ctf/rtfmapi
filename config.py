from os.path import expanduser
import configparser

config = configparser.ConfigParser()
config.read('{}/.rtfmapi/rtfmapi.conf'.format(expanduser('~')))

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

