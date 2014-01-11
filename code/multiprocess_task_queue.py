# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 22:23:21 2014

@author: Goutham
"""

from multiprocessing import Pool
from flask import Flask
	
app = Flask(__name__)
_pool = None	

def expensive_function(x):
	# do your expensive time consuming process
	return x*x
	
	
@app.route('/expensive_calc/<int:x>')
def route_expcalc(x):
    f = _pool.apply_async(expensive_function,[x])
    r = f.get(timeout=2)
    #r = expensive_function(x)
    return 'Result is %d'%r

if __name__=='__main__':
    _pool = Pool(processes=4)
    try:
        # insert production server deployment instead of app.run())
        app.run()
    except KeyboardInterrupt:
        _pool.close()
        _pool.join()
    