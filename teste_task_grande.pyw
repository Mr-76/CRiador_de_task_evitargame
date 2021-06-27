import subprocess #usar o terminal 
import os
import psutil
import sys
import time
from datetime import datetime


#btach file criar 2 strign path oythonexe e scrfipt , 
# #batch de execuçao desses ^2^^^ 
#btach de criação de task

# SCHTASKS /CREATE /SC DAILY /TN "FOLDERPATH\TASKNAME" /TR "C:\SOURCE\FOLDER\APP-OR-SCRIPT" /ST HH:MM
TODAY_DATE = datetime.now() #pegando o objeto dia de hoje
"""
https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
https://www.computerhope.com/schtasks.htm
https://www.google.com.br/search?q=how+to+package+a+python+script+it+into+a+service&sxsrf=ALeKk01DGTiKvTnENv1G02twFtZ8OC4vBg%3A1624626524187&source=hp&ei=XNXVYO6xB4DI1sQP-72z8AQ&iflsig=AINFCbYAAAAAYNXjbAhlxMWLOFJhF0qQBVt9TEsPIV73&oq=how+to+package+a+python+script+it+into+a+service&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6CAgAELEDEIMBOgUIABCxAzoLCC4QsQMQxwEQowI6AggAOgQIABBDOgUILhCxAzoCCC46CAghEBYQHRAeOgQIIRAKULIEWJ5WYNlZaABwAHgAgAHeAYgBgx-SAQYwLjIyLjKYAQCgAQGgAQKqAQdnd3Mtd2l6&sclient=gws-wiz&ved=0ahUKEwjuz_O27bLxAhUApJUCHfveDE4Q4dUDCAc&uact=5
sc - ONSTART

"""


#need a list of the programs names

PROGRAMS_NAMES = ['gta_sa.exe',"KingdomCome.exe","RocketLeague.exe","Titanfall2.exe",
                "DAOrigins.exe","survarium.exe","WatchDogs2.exe","GTA5.exe",
                "DyingLightGame.exe","Dauntless-Win64-Shipping.exe","metro.exe","vermintide2.exe"]


print(TODAY_DATE.strftime("%a")) # pegando o nome do dia de hj

if TODAY_DATE.strftime("%A") == "Saturday" or TODAY_DATE.strftime("%A") == "Sunday":
    quit()
else:
    while True:
        time.sleep(60)
        print(sys.executable)
        for p in psutil.process_iter(): # mostra taodos os processos 
            if p.name() in PROGRAMS_NAMES:
                for i in range(10):
                    print("FOUND")
                
                comand_line_code = ("taskkill /IM {} /F".format(p.name()))
                
                subprocess.Popen(comand_line_code,shell = True)# abrir terminal
                time.sleep(20)
                
                break
