import datetime
import pytz

UTC = pytz.utc
date = datetime.datetime.now(UTC)

def linecounter(incoming):
    with open(incoming) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def RPZbuilding(excluded,incoming,output):
    ankstanop = linecounter(incoming)
    with open(excluded ,'r') as f:
        exclude = f.read().split()
    with open(incoming ,'r') as f:
        lines = f.read().splitlines() # read lines
    with open(output ,'w') as f:
        f.write('; Title : Minoplhy Personal Blocklist\n')
        f.write('; Description : My Very Personal DNS Blocklist plus crawling from the source\n')
        f.write('; Source : Resources/Source.txt\n')
        f.write('; Rule Counter : ' + str(ankstanop) +' Rules\n')
        f.write('; Format : RPZ\n')
        f.write('; Licenses : MIT\n')
        f.write('; Compiled Date : ' + str(date) +'\n\n')
        f.write('$TTL 30\n')
        f.write('@ IN SOA localhost. root.localhost. (1 6h 1h 1w 2h)\n')
        f.write(' NS  localhost.\n\n')
        for line in lines:
            if line.strip() and not line in exclude and not line.startswith(';'):
               f.write('\n'.join([line + ' CNAME .\n'])) and f.write('\n'.join(['*.'+line+' CNAME .\n']))
            elif line.startswith((';','$','@','  IN')):
               f.write('\n'.join([line + '\n']))
    f.close()