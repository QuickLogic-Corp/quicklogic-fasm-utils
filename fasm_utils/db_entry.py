import csv
import argparse
from . import segbits

class DbEntry(object):


    def __init__(self, signature: str, coords: list):
        self.signature = signature
        self.coords = coords


    @classmethod
    def from_dbline(dbline: str) -> 'DbEntry':
        signature, coords = segbits.read_segbits_line(dbline)
        return cls(signature, coords)


    def __str__(self):
        res = self.signature
        for coord in self.coords:
            res += ' ' + \
                   ('' if coord.isset else '!') + \
                   str(coord.x) + '_' + str(coord.y) + '\n'
        return res
