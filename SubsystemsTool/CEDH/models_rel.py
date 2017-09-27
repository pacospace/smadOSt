#Reliability single component (no redundancy)
#Reliability series (no redundancy)
#Reliability parallel (active redundancy) 2 component
#Reliability parallel (standby redundancy) 2 component
#Reliability parallel (active redundancy)3 component
#Triple Modular Redundancy (active redundancy)
import numpy as np


def Rel_1C(FITS,Mission_L):
    lambda_p = np.divide(float(FITS),10**9)
    R_law = []
    for time in Mission_L:
        counter = 0
        if counter < len(Mission_L):
            R_law.append(np.exp(-lambda_p*time))
        counter = counter + 1
    return R_law

def Rel_2Cn(FITS,Mission_L):
    lambda_p = np.divide(float(FITS),10**9)
    R_law = []
    for time in Mission_L:
        counter = 0
        if counter < len(Mission_L):
            R_law.append(np.exp(-lambda_p*time))
        counter = counter + 1
    return np.array(R_law)*np.array(R_law)

def Rel_2Ca(FITS,Mission_L):
    lambda_p = np.divide(float(FITS),10**9)
    R_law = []
    for time in Mission_L:
        counter = 0
        if counter < len(Mission_L):
            R_law.append(np.exp(-lambda_p*time))
        counter = counter + 1
    return 1 - ((1 - np.array(R_law))*(1 - np.array(R_law)))