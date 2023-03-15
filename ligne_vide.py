import os
import re

DIR = "C:/Users/Administrateur/Downloads/"

fichier = open(DIR+"input.txt", "r")
lines = fichier.readlines()
fichier.close()

todel = []
for i in range(len(lines)) :
    if lines[i][0:2] == '\n' :
        todel.append(i)
    elif 'ECF' in lines[i] :
        todel.append(i)
todel.reverse()
for i in todel :
    lines.pop(i)

for i in range(len(lines)) :
    lines[i] = re.sub(r'\b[M]+[0-20]\b', "", lines[i])
    lines[i] = re.sub("ô", "o", lines[i])
    lines[i] = re.sub("é", " e", lines[i])
    lines[i] = re.sub("/'", "_", lines[i])
    lines[i] = re.sub("//", "_", lines[i])
    #lines[i] = re.sub([" "], "_", lines[i])

for line in lines :
    print(line, end='')

for line in lines :
    os.system('mkdir '+line)