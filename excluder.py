import crawler

def add(incoming,input):
    with open(incoming, 'r') as f:
        lines = f.read().split()
    with open(incoming, 'a') as f:
        f.write('\n'.join([input + '\n']))
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
    data += "\n"
    data += data2
    with open (incoming, 'w') as fp:
        fp.write(data)
    with open(incoming, 'r') as f:
        lines = set(f.readlines())
    with open(incoming, 'w') as f:
          f.writelines(set(lines))
    crawler.sort(incoming)