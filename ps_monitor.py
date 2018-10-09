#!/usr/bin/python3
import subprocess as sp
from time import sleep

res = sp.Popen(['ps', '-ef'], stdout=sp.PIPE, stderr=sp.PIPE)
output, error = res.communicate()
output = output.decode('ascii')
error = error.decode('ascii')

if output:
    counter = 0
    outputList = list(output.split('\n'))
    for item in outputList:
        if 'nnet3-latgen-faster' in item:
            counter += 1
    print(counter)

elif error:
    print(error)
