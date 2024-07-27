codelistenLst = []
lines = []
with open('xjustiz_3_4_1_Codelisten.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    line = lines[index]
    line = line.strip('\n\r\t')
    if 'Code-Datentyp Codeliste VersionTyp' in line:
        continue
    if 'Code.' not in line:
        continue
    if line.startswith('Code.'):
        if line[-1] == '1' or line[-1] == '3':
            if int(line[-1]) == 1 or int(line[-1]) == 3:
                codelistenLst.append(line)
        else:
            tmp = ''
            while(True):
                tmp = tmp + line
                index = index + 1
                line = lines[index]
                line = line.strip('\n\r\t')
                if line[-1] == '1' or line[-1] == '3':
                    if int(line[-1]) == 1 or int(line[-1]) == 3:
                        tmp = tmp + line
                        codelistenLst.append(tmp)
                        break
            
for codelist in codelistenLst:
    print(codelist)