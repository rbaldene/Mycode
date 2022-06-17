#!/usr/bin/env python3
import time
import os
from subprocess import call
import yaml
import crayons

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

def switchcount(switches):
   i = 0
   for switch in switches:
       i += 1
   return i

def switchstatus():
    with open("swcfg.yaml", "r") as switches:
        myswitches = yaml.safe_load(switches)
    clear()
    print(crayons.green(f"There are {switchcount(myswitches)} to configure, they are:", bold=True))
    for switch in myswitches:
        print(crayons.white(f"connecting to {switch.get('switchname')} via {switch.get('sshtarget')}", bold=True))
        for command in switch.get('commands'):
            print(crayons.blue(f"sending {command.get('command')} {command.get('subcommand')} ", bold=True))
    


def main():
    try:
        while True:
            switchstatus()
            time.sleep(2)
    except KeyboardInterrupt:
        pass


main()

