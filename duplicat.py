def add_file(input, output):
    with open(input, 'r') as f:
        lines = f.read().split()
    with open(output, 'a') as f:
        for line in lines:
            f.write('\n'.join([line + '\n']))
    f.close()
    print('Getting rid of duplicated line')
    with open(output, 'r') as f:
        lines = set(f.readlines())
    with open(output, 'w') as f:
        f.writelines(set(lines))
    f.close()

def check_n_kill_dupes(duperuleset, input):
    with open(duperuleset, 'r') as s:
        ruleset = s.read().split()
    with open(input, 'r') as f:
        lines = f.read().split()
    with open(input, 'w') as f:
        for line in lines:
            if not line in ruleset:
                f.write('\n'.join([line + '\n']))
    f.close()
    # Remove Blank Line
    with open(input ,'r') as f:
        lines = f.read().split()
    with open(input ,'w') as f:
        for line in lines:
            if line.strip():
                f.write('\n'.join([line + '\n']))
    f.close()