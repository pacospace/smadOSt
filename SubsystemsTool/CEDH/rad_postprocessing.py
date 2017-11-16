# Post Processing of the results from SPENVIS
import numpy as np
import matplotlib.pyplot as plt

file = open('resultsSPENVIS.txt', 'r')
content = file.read()
print(content)
linelist = []
lines = {}
n_line = 1

for character in content:
    linelist.append(character)
    if character == '\n':
        line = ''.join(linelist)
        lines[n_line] = line
        n_line += 1
        linelist = []

keys = list(lines.keys())
rown = 0
rowm = []
mm = np.ones((25, 6))

for key in keys[25:50]:
    row = lines[key]
    srow = row.split(',')

    for element in srow:
        rowm.append(float(element))
    matrix = np.array(rowm)
    mm[rown][:] = matrix

    rowm = []
    rown += 1

print(np.matrix(mm))
nrow = 0
Al_thickness = []
Tot_ionizing_dose = []
for row in mm:
    Al_thickness.append(mm[nrow][0])
    Tot_ionizing_dose.append(mm[nrow][1])
    nrow += 1


plt.plot(Al_thickness, [element/1000 for element in Tot_ionizing_dose])
plt.grid()
plt.xlabel('Al thickness [mm]')
plt.ylabel('Total Ionizing Dose [krad]')
plt.show()
