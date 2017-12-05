import functions
import radiation_model
import reliability_model


def main():
    # retrieve USER inputs
    CEDH_USER_inputs = functions.parseXML('USERinputCEDH.xml')

    # retrieve ADVANCED USER inputs
    CEDH_ADV_USER_inputs = functions.parseXML('ADV_USERinputCEDH.xml')

    # General inputs for more than one model
    general_USER_inputs = functions.model_inputs('general', CEDH_USER_inputs)

    # Radiation model
    rad_mod_USER_inputs = functions.model_inputs('radiation', CEDH_USER_inputs)
    radiation_model.do_rad(CEDH_ADV_USER_inputs, general_USER_inputs, rad_mod_USER_inputs)

    # Reliability model
    rel_mod_USER_inputs = functions.model_inputs('reliability', CEDH_USER_inputs)
    reliability_model.do_rel(general_USER_inputs, rel_mod_USER_inputs)

    # work in progress


if __name__ == '__main__':
    main()




