import subprocess
import os
import sys
import time

MODULOS = ("pip install datetime psutil")   

comandLineCode =  subprocess.Popen(MODULOS)

cwd = os.getcwd()  #script path


print(sys.executable.replace('python.exe', 'pythonw.exe'))

exePath = sys.executable.replace('python.exe', 'pythonw.exe')


LINHA_SCRIPT_USAR = ( (exePath) + " " + r'"{}\SETUP.py"'.format(cwd) )


nome = "PART2.bat"
f = open(nome, "w")
f.write(LINHA_SCRIPT_USAR)
f.close()

time.sleep(5)

#####
cwd = os.getcwd()  #script path
print(cwd)


#C:/Users/vluca/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/python.exe "Z:\python\Untitled-1.py"
print(sys.executable.replace('python.exe', 'pythonw.exe'))

exePath = sys.executable.replace('python.exe', 'pythonw.exe')


LINHA_SCRIPT_USAR = ( (exePath) + " " + r'"{}\teste_task_grande.pyw"'.format(cwd) )

print(LINHA_SCRIPT_USAR)#inside bat file

nome = "Executavel_game.bat"
f = open(nome, "w")
f.write(LINHA_SCRIPT_USAR)
f.close()

