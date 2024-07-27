codelistenDict = {}
lines = []
with open('xjustiz_3_4_1_Codelisten_PDF.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()

for index, _ in enumerate(lines):
    line = lines[index]
    line = line.strip('\n\r\t')
    if '.Typ3' in line:
        continue
    if line.startswith('Code.'):
        splitLine = line.split(' ')
        if splitLine[-1] == '1' or splitLine[-1] == '3':
            if int(splitLine[-1]) == 1 or int(splitLine[-1]) == 3:
                codelistenDict[splitLine[0]] = splitLine[-2]

individual_dicts = []
# Using list comprehension
individual_dicts = [{key: value} for key, value in codelistenDict.items()]

with open('codelist_vers_from_pdf.txt', 'w+', encoding='utf-8') as f:
    for d in individual_dicts:
        f.write(str(d) + '\n')

# for key in codelistenDict.keys():
#     print(key + ' = ' + codelistenDict[key])