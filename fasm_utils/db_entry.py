import csv
import argparse


class DbEntry(object):
    

    def __init__(self, signature: str, coord: tuple):
        self.signature = signature
        self.coord = coord

    @classmethod
    def from_dbline(dbline: str) -> 'DbEntry':
        signature = dbline.split(' ')[0]
        coords = tuple(map(int, dbline.split(' ')[1].split('_')))
        return cls(signature, coords)


    def __str__(self):
        return self.signature + ' ' + \
               str(self.coord[0]) + '_' + \
               str(self.coord[1]) + '\n'
