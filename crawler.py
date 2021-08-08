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

def filtering(filters_welcome):
    print("filtering . . .")
    with open(filters_welcome, 'r') as f:
        lines = f.read().splitlines()
    with open(filters_welcome, 'w') as f:
        for line in lines:
            if not line.startswith(('#',';','@','$','  NS',' NS','@@||','!')) and line.strip():
                f.write('\n'.join([line + '\n']))
        print("++ successful!")
        f.close()

def filteringcon(filters_regex_one):
    print("filtering . . .")
    with open(filters_regex_one) as f:
         file = f.read().split('\n')
         for i in range(len(file)):
             file[i] = re.sub('\s\s+#.*', '', file[i])
             file[i] = re.sub(' CNAME .$', '', file[i])
             file[i] = re.sub(' CNAME . $', '', file[i])
    with open(filters_regex_one, 'w') as f1:
         f1.writelines(["%s\n" % item  for item in file])
    print("++ successful!")
    f.close()

    a = ['||','^','|','0.0.0.0 ','0.0.0.0','::1 ','127.0.0.1 ','0','::','::1','127.0.0.1','0','::']
    lst = []
    with open(filters_regex_one, 'r') as f:
        for line in f:
            for word in a:
                if word in line and not line.startswith('#') and line.startswith((tuple(a))):
                    line = line.replace(word,'')
                else:
                    line = line.replace(line, line)
            lst.append(line)
    f.close()
    with open(filters_regex_one, 'w') as f:
        for line in lst:
            f.write(line)
        f.close()

    remove_words = ['localhost','localhost.localdomain','local','broadcasthost','loopback','ip6-localnet','ip6-mcastprefix','ip6-allnodes','ip6-allrouters','ip6-allhosts','ip6-loopback']
    
    with open(filters_regex_one, 'r') as f:
        lines = f.read().splitlines()
    with open(filters_regex_one, 'w') as f:
        for line in lines:
            if not line.endswith((tuple(remove_words))):
                f.write('\n'.join([line + '\n']))
    
    with open(filters_regex_one) as f:
        file = f.read().split('\n')
        for i in range(len(file)):
            file[i] = re.sub('\s\s+', ' ', file[i])
            file[i] = re.sub('#..*', '', file[i])
            file[i] = re.sub('CNAME . ;..*', '', file[i])
            file[i] = re.sub(';..*', '', file[i])
    with open(filters_regex_one, 'w') as f1:
        f1.writelines(["%s\n" % item  for item in file])
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
    with open(excluded ,'r') as f:
        exclude = f.read().split()
    with open(incoming ,'r') as f:
        lines = f.read().splitlines() # read lines
    with open(incoming ,'w') as f:
        for line in lines:
            if line.strip() and not line in exclude and not line.startswith(';'):
               f.write('\n'.join([line + '\n']))
            elif line.startswith((';','$','@','  IN')):
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