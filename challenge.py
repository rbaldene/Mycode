#!/usr/bin/python3

import yaml
import crayons

def main():

    with open('farms.yaml', 'r') as farmlife:
        farms = yaml.safe_load(farmlife)
        print(farms)

    print(crayons.green("Old McDonald had a farm, thay are:", bold=True))  
    for farm in farms:
        print(crayons.yellow(farm.get('name')+":" + " which are raising: ", bold=True))
        for agri in farm.get('agriculture'):
            print(crayons.blue(" - "+agri, bold=True))

main()

    




