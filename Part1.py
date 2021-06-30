#cria dois arquivos bat O STUP.bat que cria a task, e executavel_game que é executado pelo windwos task manager
import subprocess
import os
import sys

MODULOS = ("pip install datetime psutil")   

comandLineCode =  subprocess.Popen(MODULOS)

localScriptCmd = os.getcwd()#local onde o script esta sendo rodado pleo terminal



exePath = sys.executable.replace('python.exe', 'pythonw.exe') # mudar para python sem terminal


LINHA_SCRIPT_USAR = ((exePath) + " " + r'"{}\STUP.py"'.format(localScriptCmd)) # criando o path para executar
                                                                    #o script STUP.py


nome = "PARTT2.bat"
with open(nome,"w") as batP2:
    batP2.write(LINHA_SCRIPT_USAR)

LINHA_SCRIPT_USAR = ( (exePath) + " " + r'"{}\teste_task_grande.pyw"'.format(localScriptCmd))#segundo script bat

nome = "Executavel_game.bat"
with open(nome,"w") as BATex:
    BATex.write(LINHA_SCRIPT_USAR)
    
