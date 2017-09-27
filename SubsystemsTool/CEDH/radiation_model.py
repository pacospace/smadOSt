import SPENVIS_interface
import functions
import numpy as np


def do_rad(CEDH_ADV_USER_inputs, general_USER_inputs, rad_mod_USER_inputs):
    rad_mod_ADV_USER_inputs = functions.model_inputs('radiation', CEDH_ADV_USER_inputs)
    ## RADIATION Model ADVANCED USER INPUTS:
    # Username
    # Password
    # Project name (It shall be the same as SPENVIS online)
    # +- range respect to the selected inclination
    # Day of departure of the mission
    # Month of departure of the mission
    # RAAN = Right Ascension of the ascending node [deg]
    # Anomaly of the pericenter [deg]
    # True Anomaly [deg]
    # Al shielding [mm]

    # SPENVIS fixed inputs
    Orb_gen_type = 'General'

    orb_gen = 1

    lctn = 0

    Alt_vec_type = 'Specific'

    # Altitude of the circular orbit
    Altitude = functions.specific_model_input('Altitude', general_USER_inputs)

    # [degree] Inclination of the orbit
    input_Incl = functions.specific_model_input('Inclination', general_USER_inputs)

    # Lifetime for the mission
    Lifetime = functions.specific_model_input('Lifetime', general_USER_inputs)



    # range of inclinations that shall be considered
    range_ii = functions.specific_model_input('range_ii', rad_mod_ADV_USER_inputs)

    # RAAN
    OMEGA = functions.specific_model_input('OMEGA', rad_mod_ADV_USER_inputs)

    # DAY
    day = functions.specific_model_input('DAY', rad_mod_ADV_USER_inputs)

    # RAAN
    month = functions.specific_model_input('MONTH', rad_mod_ADV_USER_inputs)

    # anomaly of the pericenter
    omega = functions.specific_model_input('omega', rad_mod_ADV_USER_inputs)

    # True Anomaly
    theta = functions.specific_model_input('theta', rad_mod_ADV_USER_inputs)



    # Total Ionising Dose (TID) max
    TID_input = functions.specific_model_input('TID_input', rad_mod_USER_inputs)

    # Margin for the TID
    Margin_rad = functions.specific_model_input('Margin', rad_mod_USER_inputs)

    # Year
    year = functions.specific_model_input('YEAR', rad_mod_USER_inputs)

    # vector of inclinations considered for the analysis
    Inclination = np.arange(float(input_Incl) - float(range_ii), float(input_Incl) + float(range_ii) + 1, 1)

    step_Incl = len(Inclination)

    TID_treshold = float(TID_input) * (1 + np.divide(float(Margin_rad), 100))

    # username for SPENVIS
    username = functions.specific_model_input('username', rad_mod_ADV_USER_inputs)
    # rpassword for SPENVIS
    password = functions.specific_model_input('password', rad_mod_ADV_USER_inputs)
    # project name for SPENVIS
    proj = functions.specific_model_input('proj', rad_mod_ADV_USER_inputs)

    SPENVIS_interface.SPENVIS_interface_f(username, password, proj,Lifetime,day,month,year,Altitude,input_Incl,OMEGA,omega,theta)


