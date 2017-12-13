import models_rel
import functions
import numpy as np
import matplotlib.pyplot as plt


def do_rel(general_USER_inputs, rel_mod_USER_inputs):

    # [degree] Inclination of the orbit
    Lifetime = functions.specific_model_input('Lifetime', general_USER_inputs)

    # Failure in Time
    FITS = functions.specific_model_input('FITS', rel_mod_USER_inputs)

    # Mission Lifetime vector
    Lifetime_vect = np.arange(0, float(Lifetime),0.01)
    # Mission Lifetime vector in hours
    Mission_L = Lifetime_vect*365*24

    # Evaluate different type of reliability
    Rel_1C = models_rel.Rel_1C(FITS, Mission_L)

    Rel_2Cn = models_rel.Rel_2Cn(FITS, Mission_L)

    Rel_2Ca = models_rel.Rel_2Ca(FITS, Mission_L)

    # Plot results
    a, = plt.plot(Lifetime_vect, Rel_1C)
    b, = plt.plot(Lifetime_vect, Rel_2Cn)
    c, = plt.plot(Lifetime_vect, Rel_2Ca)
    plt.legend([a, b, c], ['single', 'series', 'parallel'])
    plt.xlabel('Mission Lifetime [y]')
    plt.ylabel('R')
    plt.title('Reliability, FITS:' + FITS)
    plt.grid()
    plt.savefig('Reliability_curve')
    plt.show(block=False)
    plt.pause(1)
    plt.close()

