import os
import sys
import requests
import re

input = sys.argv[1]

print('starting . . . ')

try:
    os.remove(input)
except OSError:
    pass

def download_filters(url):
    print("downloading: ",url)
      
    get = requests.get(url)
    if get.status_code == requests.codes.ok:
         with open(input, 'ab') as f:
          for data in get:
           f.write(data)
    return url

def filtering(filters_welcome):
    print("filtering . . .")
    with open(filters_welcome, 'r') as f:
        lines = f.read().splitlines()
    with open(filters_welcome, 'w') as f:
        for line in lines:
             if not line.startswith(('#',';','@','$','  NS','@@||','!')) and line.strip():
              f.write('\n'.join([line + '\n']))
        print("++ successful!")
        f.close()

def filteringcon(filters_regex_one):
    print("filtering . . .")
    with open(filters_regex_one) as f:
         file = f.read().split('\n')
         for i in range(len(file)):
             file[i] = re.sub(';.*', '', file[i])
             file[i] = re.sub(' CNAME .$', '', file[i])
             file[i] = re.sub(' CNAME . $', '', file[i])
    with open(filters_regex_one, 'w') as f1:
         f1.writelines(["%s\n" % item  for item in file])
    print("++ successful!")
    f.close()

    a = ['||','^','|']
    lst = []
    with open(filters_regex_one, 'r') as f:
        for line in f:
            for word in a:
                if word in line:
                    line = line.replace(word,'')
            lst.append(line)
    f.close()
    with open(filters_regex_one, 'w') as f:
        for line in lst:
            f.write(line)
    f.close()

def killingdup(duplicated_file):
    print('Getting rid of duplicated line')
    with open(duplicated_file, 'r') as f:
        lines = set(f.readlines())
    with open(duplicated_file, 'w') as f:
          f.writelines(set(lines))
    print("++ successful!")
    f.close()

download_filters("https://dbl.oisd.nl/")
download_filters("https://hosts.netlify.app/Pro/rpz.txt")
download_filters("https://filters.kylz.nl/RPZ/adguard/dns.txt")
download_filters("https://filters.kylz.nl/RPZ/adguard/cname-tracker.txt")
download_filters("https://filters.kylz.nl/RPZ/adguard/cname-original.txt")
download_filters("https://filters.kylz.nl/RPZ/stevenblack/f-s.txt")
download_filters("https://filters.kylz.nl/RPZ/someonewhocares/rpz.txt")
download_filters("https://urlhaus.abuse.ch/downloads/rpz/")
download_filters("https://github.com/easylist/easylist/raw/master/easylist/easylist_adservers.txt")
filtering(input)
filteringcon(input)
killingdup(input)

print('process completed.')
print('Location of your file is ' + input)

exit()