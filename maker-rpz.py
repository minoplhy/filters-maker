import os
import sys
import datetime
import pytz


excluded = sys.argv[1]
input = sys.argv[2]
output = sys.argv[3]
UTC = pytz.utc
date = datetime.datetime.now(UTC)

def linecounter():
    with open(input) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def RPZbuilding():
    with open(excluded ,'r') as f:
        exclude = f.read().split()
    with open(input ,'r') as f:
        lines = f.read().splitlines() # read lines
    with open(output ,'w') as f:
        f.write('; Title : Minoplhy Personal Blocklist\n')
        f.write('; Description : My Very Personal DNS Blocklist plus crawling from the source\n')
        f.write('; Source : Source.txt\n')
        f.write('; Rule Counter : ' + str(linecounter()) +' Rules\n')
        f.write('; Format : RPZ\n')
        f.write('; Licenses : MIT\n')
        f.write('; Compiled Date : ' + str(date) +'\n\n')
        f.write('$TTL 12h\n')
        f.write('@ IN SOA localhost. root.localhost. (1 6h 1h 1w 2h)\n')
        f.write('  IN NS  localhost.\n\n')
        for line in lines:
            if line.strip() and not line in exclude and not line.startswith(';'):
               f.write('\n'.join([line + ' CNAME .\n']))
            if line.startswith((';','$','@','  IN')):
               f.write('\n'.join([line + '\n']))
            if not line.strip():
               f.write('\n'.join([line + '\n']))
    f.close()
    os.remove(input)

RPZbuilding()
exit()