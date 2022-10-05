#!/usr/bin/python3

import sys
import os
import time
import json
import subprocess


def reload_smartsocket(curl_config):

    with open(curl_config) as config:
        data = json.load(config)
        dev_state,power_on,power_off,ping_perf = data['dev_state'],data['power_on'],data['power_off'],data['ping_perf']
    #Get the state of Smart Switch
    devstate = subprocess.run(dev_state, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    devstate = json.loads(devstate.stdout)
    #Perform ping and get returncode(success/fail).
    ping_result = subprocess.run(ping_perf, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
    print('Dev_State is: ', devstate['POWER'], ping_result.stdout)

    #Check ping returncode and state of Smart Socket. If ping fails, turn off Smart Socket.
    if ping_result.returncode !=0 and devstate['POWER']=='ON':
        devstate = subprocess.run(power_off, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
        devstate = json.loads(devstate.stdout)
        print('Beeline is down! Dev_State set to: ', devstate['POWER'])
        time.sleep(5)
        devstate = subprocess.run(power_on, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
        devstate = json.loads(devstate.stdout)
        time.sleep(7)
        print('Dev_State set to: ', devstate['POWER'], 'Router restarted!')
    #If Smart Socket is off, turn it on anyway.
    elif devstate['POWER']=='OFF':
        devstate = subprocess.run(power_on, shell=True, stdout=subprocess.PIPE, encoding='UTF-8')
        devstate = json.loads(devstate.stdout)
        print('Switch was disabled! Enabled! Dev_State is: ', devstate['POWER'])
    else:
        print('All is ok!')



if __name__ == "__main__":
    reload_smartsocket('/home/phil/tuya/curl_config.json')
