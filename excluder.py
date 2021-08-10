import os
import crawler

def add(incoming,userinput):
    with open(incoming, 'r') as f:
        lines = f.read().split()
    with open(incoming, 'a') as f:
        f.write('\n'.join([userinput + '\n']))
    with open(incoming, 'r') as f:
        lines = set(f.readlines())
    with open(incoming, 'w') as f:
          f.writelines(set(lines))
    crawler.sort(incoming)

def add_file(incoming,excluded_in):
    data= ""
    with open(incoming) as fp:
        data = fp.read()
    with open(excluded_in) as fp:
        data2 = fp.read()
    data += data2
    with open (incoming, 'w') as fp:
        fp.write(data + '\n')
    with open(incoming, 'r') as f:
        lines = set(f.readlines())
    with open(incoming, 'w') as f:
          f.writelines(set(lines))
    crawler.sort(incoming)
    os.remove(excluded_in)

def remove(incoming,userinput):
    with open(incoming, 'r') as f:
        lines = f.read().split()
    with open(incoming, 'w') as f:
        for line in lines:
            if line.startswith(userinput) and userinput in line:
                f.write(line.replace(userinput ,''))
            elif not line.startswith(userinput):
                f.write('\n'.join([line + '\n']))
    with open(incoming ,'r') as f:
        lines = f.read().split()
    with open(incoming ,'w') as f:
        for line in lines:
            if line.strip():
                f.write('\n'.join([line + '\n']))
    with open(incoming, 'r') as f:
        lines = set(f.readlines())
    with open(incoming, 'w') as f:
          f.writelines(set(lines))
    crawler.sort(incoming)

def remove_file(incoming ,removed_in):
    with open(removed_in ,'r') as f:
        stallin = f.read().split()
    with open(incoming, 'r') as f:
        lines = f.read().split()
    with open(incoming, 'w') as f:
        for line in lines:
            if line in stallin and line.strip() and line.startswith((tuple(stallin))):
                f.write(line.replace(line ,''))
            elif not line.startswith((tuple(stallin))):
                f.write('\n'.join([line + '\n']))
    os.remove(removed_in)

def search(incoming,userinput):
    with open(incoming, 'r') as f:
        lines = f.read().split()
        for line in lines:
            if userinput in line and line.endswith(userinput):
                print(line)
                