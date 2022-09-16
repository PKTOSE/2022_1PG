st = input()
file_dict = {'alpha':0, 'upper':0, 'lower':0, 'digit':0, 'space': 0}
for i in st:
    if i.isupper():
        file_dict['upper'] += 1
        file_dict['alpha'] += 1
    elif i.islower():
        file_dict['lower'] += 1
        file_dict['alpha'] += 1
    elif i.isdigit():
        file_dict['digit'] += 1
    elif i == ' ':
        file_dict['space'] += 1

print(file_dict)