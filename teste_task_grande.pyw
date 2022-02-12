from datetime import datetime
import subprocess #usar o terminal 
import os
import sys
import time
import psutil

TODAY_DATE = datetime.now() #pegando o objeto dia de hoje

PROGRAMS_NAMES = ['gta_sa.exe',"KingdomCome.exe","RocketLeague.exe","Titanfall2.exe",
                "DAOrigins.exe","survarium.exe","WatchDogs2.exe","GTA5.exe",
                "DyingLightGame.exe","Dauntless-Win64-Shipping.exe","metro.exe","vermintide2.exe",
                "SniperElite4_DX11.exe","DeusEx.exe"]



if TODAY_DATE.strftime("%A") == "Saturday" or TODAY_DATE.strftime("%A") == "Sunday":
    quit()
else:
    while True:
        time.sleep(60)
        for p in psutil.process_iter(): # mostra taodos os processos 
            if p.name() in PROGRAMS_NAMES:
                for i in range(10):
                    print("FOUND")
                
                comand_line_code = ("taskkill /IM {} /F".format(p.name()))
                
                subprocess.Popen(comand_line_code,shell = True)# abrir terminal
                time.sleep(20)
                
                break
