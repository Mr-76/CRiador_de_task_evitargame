%cd%

echo "Hello"



SCHTASKS /CREATE /SC ONLOGON /TN "GAME_NEVER" /TR "%~dp0teste_task_grande.exe"