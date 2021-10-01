import os
import requests
import re

def clear_old_files(incoming):
    try:
        os.remove(incoming)
    except OSError:
        pass

def download_filters(url,incoming):
    print("downloading: ",url)
      
    get = requests.get(url)
    if get.status_code == requests.codes.ok:
         with open(incoming, 'ab') as f:
          for data in get:
           f.write(data)
    return url

def download_group_filters(multi_url,incoming):
    for url in multi_url:
        print("downloading: ",url)
        
        get = requests.get(url)
        if get.status_code == requests.codes.ok:
            with open(incoming, 'ab') as f:
                for data in get:
                    f.write(data)
    return url

def filtering(filters_welcome):
    unwanted = ['#',';','@','$','  NS',' NS','@@||','!','local-data:','-']
    print("filtering . . .")
    with open(filters_welcome, 'r') as f:
        lines = f.read().splitlines()
    with open(filters_welcome, 'w') as f:
        for line in lines:
            if not line.startswith((tuple(unwanted))) and line.strip():
                f.write('\n'.join([line + '\n']))
        print("Simple Filtering Completed!")
    f.close()
    with open(filters_welcome) as f:
         file = f.read().split('\n')
         for i in range(len(file)):
             file[i] = re.sub('/..+\Z', '', file[i])
             file[i] = re.sub(':(\d\d\d\d\d|\d\d\d\d|\d\d\d|\d\d|\d)', '', file[i])
             file[i] = re.sub('(\d|\d\d|\d\d\d)\.(\d|\d\d|\d\d\d)\.(\d|\d\d|\d\d\d)\.(\d|\d\d|\d\d\d)\Z', '', file[i])
    with open(filters_welcome, 'w') as f1:
         f1.writelines(["%s\n" % item  for item in file])
    print("Ip Address and Url Path filtering Operation Completed!")
    f.close()

def filteringcon(filters_regex_one):
    print("filtering . . .")
    with open(filters_regex_one) as f:
         file = f.read().split('\n')
         for i in range(len(file)):
             file[i] = re.sub('\s\s+#.*', '', file[i])
             file[i] = re.sub(' CNAME .$', '', file[i])
             file[i] = re.sub(' CNAME . $', '', file[i])
             file[i] = re.sub('^\*.', '', file[i])
             file[i] = re.sub('^\*', '', file[i])
             file[i] = re.sub('\s\s+', ' ', file[i])
             file[i] = re.sub('#..*', '', file[i])
             file[i] = re.sub('CNAME . ;..*', '', file[i])
             file[i] = re.sub(';..*', '', file[i])
             file[i] = re.sub('\A^\.', '', file[i])
             file[i] = re.sub('^\s+|\s+$', '', file[i])
             file[i] = re.sub(' $', '', file[i])
    with open(filters_regex_one, 'w') as f1:
         f1.writelines(["%s\n" % item  for item in file])
    print("RPZ filtering operation completed!")
    f.close()
    
    with open(filters_regex_one) as f:
        file = f.read().split('\n')
        for i in range(len(file)):
            file[i] = re.sub('0\.0\.0\.0 0\.0\.0\.0\Z', '', file[i])
            file[i] = re.sub('\A127\.0\.0\.1 ', '', file[i])
            file[i] = re.sub('\A0\.0\.0\.0 ', '', file[i])
            file[i] = re.sub('\A0 ', '', file[i])
            file[i] = re.sub('\A:: ', '', file[i])
            file[i] = re.sub('\A::1 ', '', file[i])
            file[i] = re.sub('^\A\|\|', '', file[i])
            file[i] = re.sub('\^$\Z', '', file[i])
            file[i] = re.sub('^\|', '', file[i])
            file[i] = re.sub(r'#', ';', file[i])
    with open(filters_regex_one, 'w') as f1:
        f1.writelines(["%s\n" % item  for item in file])
    print('Host and Adblock filtering Operation Completed!')
    f.close() 

    with open(filters_regex_one) as f:
        file = f.read().split('\n')
        for i in range(len(file)):
            file[i] = re.sub('\Alocal-zone: "', '', file[i])
            file[i] = re.sub('static\Z', '', file[i])
            file[i] = re.sub('always_null\Z', '', file[i])
            file[i] = re.sub('always_nxdomain\Z', '', file[i])
            file[i] = re.sub('always_refuse\Z', '', file[i])
            file[i] = re.sub('redirect\Z', '', file[i])
            file[i] = re.sub('" $', '', file[i])
    with open(filters_regex_one, 'w') as f1:
        f1.writelines(["%s\n" % item  for item in file])
    print('unbound filtering Operation Completed!')
    f.close() 

    with open(filters_regex_one) as f:
        file = f.read().split('\n')
        for i in range(len(file)):
            file[i] = re.sub('\Aserver=/', '', file[i])
            file[i] = re.sub('\Aaddress=/', '', file[i])
            file[i] = re.sub('127\.0\.0\.1\Z', '', file[i])
            file[i] = re.sub('0\.0\.0\.0\Z', '', file[i])
            file[i] = re.sub('::\Z', '', file[i])
            file[i] = re.sub('::1\Z', '', file[i])
            file[i] = re.sub('/\Z', '', file[i])
            file[i] = re.sub('/$', '', file[i])
    with open(filters_regex_one, 'w') as f1:
        f1.writelines(["%s\n" % item  for item in file])
    print('dnsmasq filtering Operation Completed!')
    f.close()

    remove_words = ['localhost','localhost.localdomain','local','broadcasthost','loopback','ip6-localnet','ip6-mcastprefix','ip6-allnodes','ip6-allrouters','ip6-allhosts','ip6-loopback',' CNAME rpz-passthru.']
    
    with open(filters_regex_one, 'r') as f:
        lines = f.read().splitlines()
    with open(filters_regex_one, 'w') as f:
        for line in lines:
            if not line.endswith((tuple(remove_words))):
                f.write('\n'.join([line + '\n']))
        f.close()

def killingdup(duplicated_file):
    print('Getting rid of duplicated line')
    with open(duplicated_file, 'r') as f:
        lines = set(f.readlines())
    with open(duplicated_file, 'w') as f:
        f.writelines(set(lines))
    print("++ successful!")
    f.close()

def excluded(excluded ,incoming):
    exline = [';','$','@','  IN']
    with open(excluded ,'r') as f:
        exclude = f.read().split()
    with open(incoming ,'r') as f:
        lines = f.read().splitlines() # read lines
    with open(incoming ,'w') as f:
        for line in lines:
            if line.strip() and not line in exclude and not line.startswith(';'):
               f.write('\n'.join([line + '\n']))
            elif line.startswith((tuple(exline))):
               f.write('\n'.join([line + '\n']))
            elif not line.strip():
               f.write('\n'.join([line + '\n']))

def blankremover(incoming):
    with open(incoming ,'r') as f:
        lines = f.read().split()
    with open(incoming ,'w') as f:
        for line in lines:
            if line.strip():
                f.write('\n'.join([line + '\n']))

def sort(incoming):
    with open(incoming, 'r') as f:
        lines = sorted(f.readlines())
    with open(incoming, 'w') as f:
        for line in lines:
            f.write(line)