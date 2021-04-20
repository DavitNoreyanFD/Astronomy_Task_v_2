import configparser


config = configparser.ConfigParser()
config.read('config.ini')

data_file = config['USER']['datafile']
fov_v = float(config['USER']['fov_v'])
fov_h = float(config['USER']['fov_h'])
ra_user = float(config['USER']['ra_user'])
dec_user = float(config['USER']['dec_user'])
n = int(config['USER']['n'])


class Star:
    def __init__(self, star_id, ra, dec, mag, flux):
        self.id = star_id
        self.ra = ra
        self.dec = dec
        self.mag = mag
        self.flux = flux
        self.distance = ((self.ra-fov_v)**2+(self.dec-fov_h)**2)**0.5

    def __repr__(self):
        return f'{self.id}, {self.ra}, {self.dec}, {self.mag}, {self.flux}, {self.distance}'
