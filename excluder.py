import os
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
    with open(incoming, "wb") as outfile:
           with open(excluded_in, "rb") as infile:
                outfile.write(infile.read())
    with open(incoming, 'r') as f:
        lines = set(f.readlines())
    with open(incoming, 'w') as f:
          f.writelines(set(lines))
    crawler.sort(incoming)
    os.remove(excluded_in)