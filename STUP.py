#Adiciona a task ao windows

import subprocess #usar o terminal 
import os
import psutil
import sys

path = os.path.realpath(__file__) # recebe o real path do sctip porque esse é executado em admin mode


nome = "Executavel_game.bat"

path = path.replace("STUP.py","") #mudar o final do path ex: z\pyhon\script.py para z\python\

scriptPath = (r'"{}{}"'.format(path,nome)) #String para coonter o local do Executavel_game




#criação dos comandos de task
PRIMEIRO_COD_TASK = (r'SCHTASKS /CREATE /SC ONLOGON /TN "GAME_NEVERHH" /TR ')
SEGUNDO_COD_TASK = scriptPath


FINAL_COD_TASK = PRIMEIRO_COD_TASK + SEGUNDO_COD_TASK

#codigo executado no cmd como admin task manger so deixa mexer se for admin :(
subprocess.Popen(FINAL_COD_TASK,shell = True)
