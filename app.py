from datetime import date
from math import radians as rad,degrees as deg
import re

from bottle import Bottle, route, run
import pyephem

import json

# import Moon


@route('/hello')
def hello():
    return "Hello World!"


@route('/moon/<dateStr:re:(\d{4})[/.-](\d{1,2})[/.-](\d{1,2})>/<latidute:re:(-?\d{1,2}[.]\d{6})>/<longitude:re:(-?\d{1,2}[.]\d{6})>')
def moon(dateStr, latitude, longitude):
    g = ephem.Observer()
    g.lat = latitude
    g.lon = longitude



    m = ephem.Moon()


    return dateStr + " " + latitude + " " + longitude


run(host='localhost', port=8080, debug=True)
