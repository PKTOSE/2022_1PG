input_path = 'input.txt'
output_path = 'output.txt'

with open(input_path) as file:
    lines = file.readlines()

with open(output_path, 'w') as writeF:
    for i in range(len(lines)):
        line = str(i) + ': '+ lines[i]
        writeF.writelines(line)

