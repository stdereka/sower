# sower
Python script which allows you to run any other script on client's machine with sudo. Простой Python-скрипт, который при
удачном стечении обстоятельств позволяет выполнить любое действие на машине
клиента с правами sudo.
# usage
usage: sower.py [-h] [-p PATH] [-c COMMAND] [-r]

optional arguments:
>*  ***-h, --help***           | show this help message and exit
>*  ***-p PATH, --path PATH*** | path to script or executable file (target)
>*  ***-c COMMAND, --command COMMAND*** | command to launch target ("sh", "python3" etc.)
>*  ***-r, --remove***         | remove "sower.py" and target (done automatically)
