# Post Processing of the results from SPENVIS TID
import matplotlib.pyplot as plt
import re


def rad_post_process():
    file = open('resultsSPENVIS.txt')
    content = file.read()
    lines = re.findall(r'\d\.\d+\w[+\-]\d+', content)

    step = 0
    row = []
    table = []
    for line in lines[1:]:
        row.append(float(line))
        step += 1
        if step == 6:
            table.append(row)
            step = 0
            row = []
        else:
            pass

    Al_thickness = []
    TID = []
    for l in table:
        Al_thickness.append(l[0])
        TID.append(l[1]/1000)  # krad

    plt.semilogy(Al_thickness, [element for element in TID])
    plt.grid()
    plt.xlabel('Al thickness [mm]')
    plt.ylabel('Total Ionizing Dose [krad]')
    plt.legend('Total Ionizing Dose')
    plt.savefig('TID_curve')
    plt.show(block=False)
    # plt.pause(1)
    plt.close()


if __name__ == '__main__':
    rad_post_process()
