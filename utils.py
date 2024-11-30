SPEC = '.+-=!()[]{}'

def escape(s):
    new = ''
    for c in s:
        if c in SPEC: new += '\\'
        new += c
    return new
