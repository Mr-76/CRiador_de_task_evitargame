import subprocess  
import os
import psutil
import sys
import time
from datetime import datetime


TODAY_DATE = datetime.now() #pegando o objeto dia de hoje



#lista de jogos precisa executar e ver no processos o nome 
PROGRAMS_NAMES = ['gta_sa.exe',"KingdomCome.exe","RocketLeague.exe","Titanfall2.exe",
                "DAOrigins.exe","survarium.exe","WatchDogs2.exe","GTA5.exe",
                "DyingLightGame.exe","Dauntless-Win64-Shipping.exe","metro.exe","vermintide2.exe",
                "SniperElite4_DX11.exe","DeusEx.exe"]


#   Me da o dia de hoje 
if TODAY_DATE.strftime("%A") == "Saturday" or TODAY_DATE.strftime("%A") == "Sunday":
    quit()
else:
    while True:
        time.sleep(60) #rodar a cada 60 seg 
        for processo in psutil.process_iter(): # mostra taodos os processos 
            if processo.name() in PROGRAMS_NAMES:
                
                # 'mata' o processo
                comand_line_code = ("taskkill /IM {} /F".format(processo.name()))
                
                subprocess.Popen(comand_line_code,shell = True)#exec codigo
                time.sleep(20)
                break#sair do for e procurar outro processo

"""
https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
https://www.computerhope.com/schtasks.htm
https://www.google.com.br/search?q=how+to+package+a+python+script+it+into+a+service&sxsrf=ALeKk01DGTiKvTnENv1G02twFtZ8OC4vBg%3A1624626524187&source=hp&ei=XNXVYO6xB4DI1sQP-72z8AQ&iflsig=AINFCbYAAAAAYNXjbAhlxMWLOFJhF0qQBVt9TEsPIV73&oq=how+to+package+a+python+script+it+into+a+service&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6CAgAELEDEIMBOgUIABCxAzoLCC4QsQMQxwEQowI6AggAOgQIABBDOgUILhCxAzoCCC46CAghEBYQHRAeOgQIIRAKULIEWJ5WYNlZaABwAHgAgAHeAYgBgx-SAQYwLjIyLjKYAQCgAQGgAQKqAQdnd3Mtd2l6&sclient=gws-wiz&ved=0ahUKEwjuz_O27bLxAhUApJUCHfveDE4Q4dUDCAc&uact=5
sc - ONSTART

"""

