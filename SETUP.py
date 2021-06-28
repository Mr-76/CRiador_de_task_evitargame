#Adiciona a task ao windows
import subprocess #usar o terminal 
import os
import sys
import time
from datetime import datetime
import psutil


with open("thepath.txt","r") as path:
    local = path.read()

print(local)

time.sleep(100000)
NOME = "Executavel_game.bat"

scriptPath = r'"{}\{}"'.format(local,NOME) #colocar isso no task

#Criando as task no windows cmd
PRIMEIRO_COD_TASK = (r'SCHTASKS /CREATE /SC ONLOGON /TN "GAME_EVITAR" /TR ')
SEGUNDO_COD_TASK = scriptPath

FINAL_COD_TASK = PRIMEIRO_COD_TASK+SEGUNDO_COD_TASK

subprocess.Popen(FINAL_COD_TASK,shell = True) #abre o terminal e coloca a task




