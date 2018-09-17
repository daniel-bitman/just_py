#!/usr/bin/env python3

#importing libs
import time

""" #vars
start_time = time.localtime()
print(f'timer started at {time.strftime("%X",start_time)}')

# wait for user for stop script
input('print anyy ey to stop script -->')

stop_time = time.localtime()
dif = time.mktime(stop_time)-time.mktime(start_time)

print(f'timer stopped at {time.strftime("%X",stop_time)}')
print(f'total time: {dif} seconds') """

from os import getenv
from os import environ
# export VARNAME="my value"
#print(environ)
stage = environ['VARNAME'].upper()

output='we are runnning in {}'.format(stage)

if stage.startswith('PROD'):
    output='DANGER -------> running on Prodaction'

print(output)