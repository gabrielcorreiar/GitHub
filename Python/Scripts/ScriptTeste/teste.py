s = 'olá mundo! 987654321o'
d = {'DIGITS': 3,'LETTERS':0}

for c in s:
    if c.isdigit():
        d['DIGITS'] += 1
    elif c.isalpha():
        d['LETTERS'] += 1
    else:
        pass

print('LETRAS', d['LETTERS'])
print('DIGITOS', d['DIGITS'])