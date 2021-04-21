"""
All constants and imported variables were collected in this module.
"""
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

data_file = config['USER']['data_file']
fov_v = float(config['USER']['fov_v'])
fov_h = float(config['USER']['fov_h'])
ra_user = float(config['USER']['ra_user'])
dec_user = float(config['USER']['dec_user'])
n = int(config['USER']['n'])


INDEX_ID = 7
INDEX_RA = 0
INDEX_DEC = 1
INDEX_MAG = 22
INDEX_FLUX = 20
