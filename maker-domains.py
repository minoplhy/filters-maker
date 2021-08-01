import os
import sys
import datetime
import pytz


excluded = sys.argv[1]
input = sys.argv[2]
UTC = pytz.utc
date = datetime.datetime.now(UTC)

def linecounter():
    with open(input) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

ankstanop = linecounter()

def domainsbuilding():
    with open(excluded ,'r') as f:
        exclude = f.read().split()
    with open(input ,'r') as f:
        lines = f.read().splitlines() # read lines
    with open(input ,'w') as f:
        f.write('# Title : Minoplhy Personal Blocklist\n')
        f.write('# Description : My Very Personal DNS Blocklist plus crawling from the source\n')
        f.write('# Source : Resources/Source.txt\n')
        f.write('# Rule Counter : ' + str(ankstanop) +' Rules\n')
        f.write('# Format : Domains\n')
        f.write('# Licenses : MIT\n')
        f.write('# Compiled Date : ' + str(date) +'\n\n')
        for line in lines:
            if line.strip() and not line in exclude and not line.startswith('#'):
               f.write('\n'.join([line + '\n']))
            if line.startswith((';','$','@','  IN')):
               f.write('\n'.join([line + '\n']))
            if not line.strip():
               f.write('\n'.join([line + '\n']))
    f.close()

domainsbuilding()
exit()