from datetime import date, datetime

from bottle import Bottle, route, run
import ephem


@route('/hello')
def hello():
    return "Hello World!"


# <dateStr:re:(\d{4})[/.-](\d{1,2})[/.-](\d{1,2})>/
# <latitude:re:(-?\d{1,2}[.]\d{6})>
# <longitude:re:(-?\d{1,2}[.]\d{6})>

@route('/moon')
def moon():
    m = ephem.Moon()
    m.compute(datetime.utcnow())

    phase = m.moon_phase

    colong = m.colong

    nnm = ephem.next_new_moon(datetime.utcnow())
    nfm = ephem.next_full_moon(datetime.utcnow())

    result = {'next_new_moon': str(nnm), 'next_full_moon': str(nfm), 'visibility': str(phase), 'colong': str(colong)}

    return result


run(host='localhost', port=61113, debug=True)
