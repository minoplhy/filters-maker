import os
import sys
import requests
import re

print('starting . . . ')

try:
    os.remove(input)
except OSError:
    pass

def download_filters(url,input):
    try:
        os.remove(input)
    except OSError:
        pass
    
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

exit()