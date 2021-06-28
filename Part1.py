import subprocess
import os
import sys

MODULOS = ("pip install datetime psutil")   #instala os modulos que não vem com python

comandLineCode =  subprocess.Popen(MODULOS) #instalando os modulos

local = os.getcwd()  #Obtendo o local onde esta esse script



exePath = sys.executable.replace('python.exe', 'pythonw.exe') #obtendo o local do execu                                                             tavel python e trocando pa                                                              ra pythonw.exe pois esse                                                        não abre um terminal quando roda


linhaScriptUsar = ((exePath) + " " + r'"{}\SETUP.py"'.format(local)) # criando string comlocal "path" do script com setup


NOME = "PART2.bat" #criando arquivo bat com as linhas de codigo anteriores
with open(NOME,"w") as ARQUIVO_BAT1
    ARQUIVO_BAT1.write(linhaScriptUsar)



#####

linhaScriptUsar = ((exePath) + " " + r'"{}\teste_task_grande.pyw"'.format(local))
#essa outra linha faz referencia a execução do codigo pelo windows
NOME = "Executavel_game.bat"
with open(NOME,"w") as ARQUIVO_BAT2
    ARQUIVO_BAT2.write(linhaScriptUsar)
quit()
