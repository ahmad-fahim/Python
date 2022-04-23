# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:49:39 2019

@author: fahim.ahmad
"""
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0

# test call
# 10.128.89.97    

while(True):
    ping_statue = ping("10.64.20.5")
    if ping_statue == True:
        winsound.Beep(frequency, duration)
        print("10.64.20.5")
        print(ping("10.64.20.5"))
         
        
        

