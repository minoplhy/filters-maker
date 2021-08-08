import datetime
import pytz

UTC = pytz.utc
date = datetime.datetime.now(UTC)

def linecounter(incoming):
    with open(incoming) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def hostsbuilding(excluded ,incoming ,output):
    ankstanop = linecounter(incoming)
    with open(excluded ,'r') as f:
        exclude = f.read().split()
    with open(incoming ,'r') as f:
        lines = f.read().splitlines() # read lines
    with open(output ,'w') as f:
        f.write('# Title : Minoplhy Personal Blocklist\n')
        f.write('# Description : My Very Personal DNS Blocklist plus crawling from the source\n')
        f.write('# Source : Resources/Source.txt\n')
        f.write('# Rule Counter : ' + str(ankstanop) +' Rules\n')
        f.write('# Format : Hosts\n')
        f.write('# Licenses : MIT\n')
        f.write('# Compiled Date : ' + str(date) +'\n\n')
        f.write('127.0.0.1 localhost\n')
        f.write('127.0.0.1 localhost.localdomain\n')
        f.write('127.0.0.1 local\n')
        f.write('255.255.255.255 broadcasthost\n')
        f.write('::1 localhost\n')
        f.write('::1 ip6-localhost\n')
        f.write('::1 ip6-loopback\n')
        f.write('fe80::1%lo0 localhost\n')
        f.write('ff00::0 ip6-localnet\n')
        f.write('ff00::0 ip6-mcastprefix\n')
        f.write('ff02::1 ip6-allnodes\n')
        f.write('ff02::2 ip6-allrouters\n')
        f.write('ff02::3 ip6-allhosts\n')
        f.write('0.0.0.0 0.0.0.0\n\n\n')
        
        for line in lines:
            if line.strip() and not line in exclude and not line.startswith('#'):
               f.write('\n'.join(['0.0.0.0 ' + line + '\n']))
            elif line.startswith((';','$','@','  IN')):
               f.write('\n'.join([line  + '\n']))
            elif not line.strip():
               f.write('\n'.join([line + '\n']))
    f.close()