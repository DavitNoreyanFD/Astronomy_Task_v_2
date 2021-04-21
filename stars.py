"""
a class of stars is written in this module
"""
import const_and_inp


class Star:
    def __init__(self, star_id, ra, dec, mag):
        """
        the star object characterizes 5 attributes, id, ra, dec, mag and distance,
        the distance we count as having ra and dec
        """
        self.id = star_id
        self.ra = ra
        self.dec = dec
        self.mag = mag
        self.distance = ((self.ra-const_and_inp.fov_v)**2 +
                         (self.dec-const_and_inp.fov_h)**2)**0.5

    def __repr__(self):
        return f'{self.id}, {self.ra}, {self.dec}, {self.mag}, {self.distance}'
