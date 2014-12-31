# -*- coding: utf-8 -*-
from geolocation.parser import Parser


class DistanceMatrixParser(Parser):
    @property
    def rows(self):
        return self.json_data.get('rows')


    @property
    def elements(self):
        for item in self.rows():
            print item