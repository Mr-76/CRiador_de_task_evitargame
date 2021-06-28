#Adiciona a task ao windows

import subprocess #usar o terminal 
import os
import psutil
import sys
import time
from datetime import datetime



cwd = os.getcwd()  #script path

print(cwd)

#need to read a file withj the path

nome = "Executavel_game.bat"

scriptPath = r'"{}\{}"'.format(cwd,nome) #colocar isso no task

print(scriptPath,"path")

#rodar 1 vez 


#e tb comando de criaçao da task
PRIMEIRO_COD_TASK = (r'SCHTASKS /CREATE /SC ONLOGON /TN "GAME_EVITAR" /TR ')
SEGUNDO_COD_TASK = scriptPath
print(SEGUNDO_COD_TASK)

FINAL_COD_TASK = PRIMEIRO_COD_TASK+SEGUNDO_COD_TASK

print(FINAL_COD_TASK)

#subprocess.Popen(FINAL_COD_TASK,shell = True)