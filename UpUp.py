n = raw_input()
def capitalize(line):
    return ' '.join(s[0].upper() + s[1:] for s in line.split(' '))
print capitalize(n)
