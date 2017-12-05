# Post Processing of the results from SPENVIS
import matplotlib.pyplot as plt
import re


def main():
    file = open('resultsSPENVIS.txt')
    content = file.read()
    linelist = re.findall(r'\d\.\d+\w[+\-]\d+', content)

    step = 0
    row = []
    table = []
    for line in linelist[1:]:
        row.append(float(line))
        step += 1
        if step == 6:
            table.append(row)
            step = 0
            row = []
        else:
            pass

    Al_thickness = []
    Tot_ion_dose = []
    for l in table:
        Al_thickness.append(l[0])
        Tot_ion_dose.append(l[1])

    plt.plot(Al_thickness, [element for element in Tot_ion_dose])
    plt.grid()
    plt.xlabel('Al thickness [mm]')
    plt.ylabel('Total Ionizing Dose [krad]')
    plt.show()


if __name__ == '__main__':
    main()
