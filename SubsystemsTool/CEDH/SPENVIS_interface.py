#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%      FUNCTION       %%%%%%%%%%%%%%%%%%%
#
#   user = username SPENVIS                        external INPUT %%%%
#   password = password SPENVIS                    external INPUT %%%%
#   proj = project name SPENVIS                    external INPUT %%%%
#   lifetime = mission lifetime [number of years]  external INPUT %%%%
#   day = day starting the mission                 external INPUT %%%%
#   month = month starting of the mission          external INPUT %%%%
#   h = altitude circular orbit                    external INPUT %%%%
#   i = inclination circular orbit                 external INPUT %%%%
#   Al_eq = equivalent Al shielding                external INPUT %%%%
#   n_devices = number of new devices              external INPUT %%%%
#   data_devices = data of the the devices         external INPUT %%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%     DESCRIPTION       %%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   ATTENTION!! It's necessary to run SPENVIS with the same project name
#   inserted in SPENVIS by the user
# 
#   user = username SPENVIS           external INPUT %%%%%%%%%%%%%%%%%
#   password = password SPENVIS       external INPUT %%%%%%%%%%%%%%%%%
#   proj = project name SPENVIS       external INPUT %%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%   orbit generator  %%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT 1 %%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Planet --> Earth
#   Trajectory Generation --> use orbit generator
#   Number of mission segments: --> 1
#   Mission End --> total mission duration ---> number of years -->
#
#   lifetime = number of years        external INPUT %%%%%%%%%%%%%%%%%
#
#   Satellite orientation: --> one axis parallel to the velocity vector
#   Account for solar radiation pressure: --> no
#   Account for atmospheric drag: --> no
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT 2 %%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Segment title --> (no title)
#   Orbit type --> general
#   orbit start -->
#
#   calendare date --> [dd/mm/yyyy]]    external INPUT %%%%%%%%%%%%%%%
#
#   Hour --> [00:00:00]
#   Representative --> trajectory duration --> 1
#   Altitude specification --> altitude for a circular orbit
#
#   Altitude [km] -->                   external INPUT %%%%%%%%%%%%%%%
#   Inclination [deg] -->               external INPUT %%%%%%%%%%%%%%%
#
#   R. asc. of asc. node [deg w.r.t. gamma50] --> 0
#   Argument of perigee [deg] --> 0
#   %Output resolution --> default
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  saving INPUT   %%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Run
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%% Radiation Sources and effects  %%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%% Radiation sources  %%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%% Trapped Proton and Electron Fluxes  %%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT %%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %standard models
#   Proton model --> AP-8
#   Electron model --> AE-8
#   Model version (proton) --> solar maximum
#   Threshold flux for exposure (proton) --> 1
#   Model version (electron) --> solar maximum
#   do not include local time variation
#   Confidence level --> 50.000%
#   Threshold flux for exposure (electron) --> 1
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%% Short-term solar particle fluxes (only for SEU)  %%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT %%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Solar particle flux model --> CREME-96
#   ion range --> H to Ni
#   worst day
#   Magnetic shielding --> default
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%% Long-term solar particle fluences  %%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT %%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Solar particle model --> ESP-PSYCHIC (total fluence)
#   ion range --> H to Ni
#   Prediction period --> automatic
#   offset in solar cycle --> automatic
#   Confidence level [%] --> 95.0
#   Magnetic shielding --> default
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%% Galactic cosmic ray fluxes  %%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT %%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   ion range --> H to Ni
#   GCR model at 1 AU--> ISO 15390
#   model -->ISO-15390 standard model
#   solar activity data --> mission epoch
#   Magnetic shielding --> default
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%% Long-term radiation doses  %%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%% Ionizing dose for simple geometries  %%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT  %%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Shielding depths --> table of values
#   Al shielding -->                   external INPUT %%%%%%%%%%%%%%%
#   Dose model --> SHIELDOSE-2
#   Shielding configuration --> centre of Al spheres
#   Target material --> Silicon
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%% Single Event Effects  %%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%% Short-term SEU rates and LET spectra  %%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT  %%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Device number (max 15) --->           INPUT external %%%%%%%%%%%
#   Device material --> Si (CREME-86)
#   Device source --> user defined
#   Device Name --->                      INPUT external %%%%%%%%%%%
#   Shape Sensitive volume ---> rectangular parallelepiped (3D)
#   Dimensions -->                        INPUT external %%%%%%%%
#   %%%%Models Weibull function and Bendel function (cross section methods)
#   Drirect ionization upset rates --->   INPUT external %%%%%%%%%%%
#   Algorithm --> constant LET (CREME)
#   %%%%%Models Weibull function and Bendel function
#   Proton induced upset rates -->        INPUT external %%%%%%%%%%%
#
#   % solar particles  + trapped protons + GCR particles
#   mission segment averages
# 
#   Al Equivalent shielding -->           INPUT external %%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%% Long-term SEU rates and LET spectra  %%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%  internal INPUT  %%%%%%%%%%%%%%%%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#   Device number (max 15) --->           INPUT external %%%%%%%%%%%
#   Device material --> Si (CREME-86)
#   Device source --> user defined
#   Device Name --->                      INPUT external %%%%%%%%%%%
#   Shape Sensitive volume ---> rectangular parallelepiped (3D)
#   Dimensions -->                        INPUT external %%%%%%%%
#   %%%%Models Weibull function and Bendel function (cross section methods)
#   Drirect ionization upset rates --->   INPUT external %%%%%%%%%%%
#   Algorithm --> constant LET (CREME)
#   %%%%Models Weibull function and Bendel function
#   Proton induced upset rates -->        INPUT external %%%%%%%%%%%
#
#   solar particles  + trapped protons + GCR particles
#   mission segment averages
#   Al Equivalent shielding -->           INPUT external %%%%%%%%%%%
#   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import requests


def do_post(url, user, password, values):
    return requests.post(url, data=values, auth=(user, password))


def SPENVIS_interface_f(user, password, proj, lifetime, day, month, year, h, i, OMEGA, omega, theta):
    url = 'https://www.spenvis.oma.be/htbin/spenvis.exe/' + proj
    # personal username shall be selected by the user and inserted in ADV_USERinputCEDH.xml for radiation model
    values = {
        'action': 'cleanup',
        'SWITCH': '1',
        'TODELETE': proj,
        '#cleanUp()#deleteFile(project.cgi)#ResetToPrevious(packages.html)': 'Execute'}

    # ('Delete previous results')
    do_post(url, user, password, values)

    # ('Orbit Generator...');
    # ('Input #1');

    values = {
        '_JS_SUBMIT': '#saveform(sapre_mis.html)#resetToPrevious(sapre_mis.html)',
        'PLANET': '3',
        'ORBGEN': '1',
        'NTRAJ': '1',
        'IMISD': '0',
        'MISDUR': lifetime,
        'JMISD':'0',
        'KATT':'2',
        'ISRP':'0',
        'IDRAG':'0',
        '#deleteFile(orbitp.cgi)#saveForm(sapre_mis.html,orbitn)#saveForm(sapre_mis.html)#ResetToPrevious(sapre_orb.html,orbit1)': 'Next >>',
        'PRODEF': proj,
        'PROTIT': '',
        'ORBITN': '0'}

    do_post(url, user, password, values)

    # ('General circular orbit')

    # ('Input #2...')

    values = {
        '_JS_SUBMIT': '#saveform(sapre_orb.html,orbit1)#resetToPrevious(sapre_orb.html,orbit1)',
        'TITLE': '',
        'TYPE': 'GEN',
        'ISTART': '1',
        'OEDAY': day,
        'OEMON': month,
        'OEYEAR': year,
        'OEHRS': '0',
        'OEMIN': '0',
        'OESEC': '0',
        'IDUR': '1',
        'EPDUR': '1',
        'IAE': '2',
        'ALT': h,
        'RINCL': i,
        'IAN': '0',
        'RAAN': OMEGA,
        'ARGPER': omega,
        'TRANO': theta,
        'DT1': '60.0',
        'DH2': '20000.0',
        'DT2': '240.0',
        'DH3': '80000.0',
        'DT3': '3600.0',
        'ORBITN': '1',
        '#saveForm(sapre_orb.html,orbit1)#deleteFile(orbitp.cgi)#saveForm(sapre_orb.html,orbitn)#ResetToPrevious(sapre_sum.html)': 'Next >>',
        'STEP': '0.5'}

    do_post(url, user, password, values)

    # ('Saving inputs...')
    values = {
        '_JS_SUBMIT': '#saveform(sapre_sum.html)#resetToPrevious(sapre_sum.html)',
        'ORBITN': '2',
        '#deleteFile(orbitn.cgi)#saveForm(sapre_sum.html,orbitp)#saveForm(sapre_sum.html)#namelist(mission[sapre_mis],sapre[orbit1])#runModel(sapre)#ResetToPrevious(sapre_out.html)': 'Run'}

    do_post(url, user, password, values)

    # ('Radiation sources')

    # ('Trapped Proton and Electron Fluxes...')
    values = {
        '_JS_SUBMIT': '#saveform(trep_par.html)#resetToPrevious(trep_par.html)',
        'TRPMOD': '1',
        'TREMOD': '1',
        'MINDP': '1',
        'FLUXTHP': '1.00',
        'MINDE': '1',
        'ILTV': '0',
        'ISIG': '0',
        'FLUXTHE': '1.00',
        '#saveForm(trep_par.html)#namelist(trep[trep_par.html])#deleteFile(ae9ap9_par.cgi)#runModel(trep)#ResetToPrevious(trep_out.html)': 'Run',
        'NENERP': '30',
        'PROEN(1)': '0.1',
        'PROEN(2)': '0.15',
        'PROEN(3)': '0.2',
        'PROEN(4)': '0.3',
        'PROEN(5)': '0.4',
        'PROEN(6)': '0.5',
        'PROEN(7)': '0.6',
        'PROEN(8)': '0.7',
        'PROEN(9)': '1.0',
        'PROEN(10)': '1.5',
        'PROEN(11)': '2.0',
        'PROEN(12)': '3.0',
        'PROEN(13)': '4.0',
        'PROEN(14)': '5.0',
        'PROEN(15)': '6.0',
        'PROEN(16)': '7.0',
        'PROEN(17)': '10.0',
        'PROEN(18)': '15.0',
        'PROEN(19)': '20.0',
        'PROEN(20)': '30.0',
        'PROEN(21)': '40.0',
        'PROEN(22)': '50.0',
        'PROEN(23)': '60.0',
        'PROEN(24)': '70.0',
        'PROEN(25)': '100.0',
        'PROEN(26)': '150.0',
        'PROEN(27)': '200.0',
        'PROEN(28)': '300.0',
        'PROEN(29)': '400.0',
        'PROEN(30)': '500.0',
        'NENERE': '30',
        'ELEEN(1)': '0.04',
        'ELEEN(2)': '0.1',
        'ELEEN(3)': '0.2',
        'ELEEN(4)': '0.3',
        'ELEEN(5)': '0.4',
        'ELEEN(6)': '0.5',
        'ELEEN(7)': '0.6',
        'ELEEN(8)': '0.7',
        'ELEEN(9)': '0.8',
        'ELEEN(10)': '1.0',
        'ELEEN(11)': '1.25',
        'ELEEN(12)': '1.5',
        'ELEEN(13)': '1.75',
        'ELEEN(14)': '2.0',
        'ELEEN(15)': '2.25',
        'ELEEN(16)': '2.5',
        'ELEEN(17)': '2.75',
        'ELEEN(18)': '3.0',
        'ELEEN(19)': '3.25',
        'ELEEN(20)': '3.5',
        'ELEEN(21)': '3.75',
        'ELEEN(22)': '4.0',
        'ELEEN(23)': '4.25',
        'ELEEN(24)': '4.5',
        'ELEEN(25)': '4.75',
        'ELEEN(26)': '5.0',
        'ELEEN(27)': '5.5',
        'ELEEN(28)': '6.0',
        'ELEEN(29)': '6.5',
        'ELEEN(30)': '7.0'}

    do_post(url, user, password, values)

    # ('Short-term solar particle fluxes...')

    values = {
        '_JS_SUBMIT': '#saveform(sepflare_par.html)#resetToPrevious(sepflare_par.html)',
        'FLAREMOD': '1',
        'ION1': '1',
        'ION2': '92',
        'CREME96': '2',
        '#saveForm(sepflare_par.html)#namelist(sepflare[sepflare_par+magshielding_par])#RunModel(sepflare)#ResetToPrevious(sepflare_out.html)': 'Run',
        'NENERS': '75',
        'ENERFL(1)': '0.10',
        'ENERFL(2)': '0.11',
        'ENERFL(3)': '0.12',
        'ENERFL(4)': '0.14',
        'ENERFL(5)': '0.16',
        'ENERFL(6)': '0.18',
        'ENERFL(7)': '0.20',
        'ENERFL(8)': '0.22',
        'ENERFL(9)': '0.25',
        'ENERFL(10)': '0.28',
        'ENERFL(11)': '0.32',
        'ENERFL(12)': '0.35',
        'ENERFL(13)': '0.40',
        'ENERFL(14)': '0.45',
        'ENERFL(15)': '0.5',
        'ENERFL(16)': '0.55',
        'ENERFL(17)': '0.63',
        'ENERFL(18)': '0.71',
        'ENERFL(19)': '0.80',
        'ENERFL(20)': '0.90',
        'ENERFL(21)': '1.0',
        'ENERFL(22)': '1.1',
        'ENERFL(23)': '1.2',
        'ENERFL(24)': '1.4',
        'ENERFL(25)': '1.6',
        'ENERFL(26)': '1.8',
        'ENERFL(27)': '2.0',
        'ENERFL(28)': '2.2',
        'ENERFL(29)': '2.5',
        'ENERFL(30)': '2.8',
        'ENERFL(31)': '3.2',
        'ENERFL(32)': '3.5',
        'ENERFL(33)': '4.0',
        'ENERFL(34)': '4.5',
        'ENERFL(35)': '5.0',
        'ENERFL(36)': '5.5',
        'ENERFL(37)': '6.3',
        'ENERFL(38)': '7.1',
        'ENERFL(39)': '8.0',
        'ENERFL(40)': '9.0',
        'ENERFL(41)': '10.0',
        'ENERFL(42)': '11.0',
        'ENERFL(43)': '12.0',
        'ENERFL(44)': '14.0',
        'ENERFL(45)': '16.0',
        'ENERFL(46)': '18.0',
        'ENERFL(47)': '20.0',
        'ENERFL(48)': '22.0',
        'ENERFL(49)': '25.0',
        'ENERFL(50)': '28.0',
        'ENERFL(51)': '32.0',
        'ENERFL(52)': '35.0',
        'ENERFL(53)': '40.0',
        'ENERFL(54)': '45.0',
        'ENERFL(55)': '50.0',
        'ENERFL(56)': '55.0',
        'ENERFL(57)': '63.0',
        'ENERFL(58)': '71.0',
        'ENERFL(59)': '80.0',
        'ENERFL(60)': '90.0',
        'ENERFL(61)': '100.0',
        'ENERFL(62)': '110.0',
        'ENERFL(63)': '120.0',
        'ENERFL(64)': '140.0',
        'ENERFL(65)': '160.0',
        'ENERFL(66)': '180.0',
        'ENERFL(67)': '200.0',
        'ENERFL(68)': '220.0',
        'ENERFL(69)': '250.0',
        'ENERFL(70)': '280.0',
        'ENERFL(71)': '320.0',
        'ENERFL(72)': '350.0',
        'ENERFL(73)': '400.0',
        'ENERFL(74)': '450.0',
        'ENERFL(75)': '500.0'}

    do_post(url, user, password, values)

    # ('Long-term solar particle fluences...');

    values = {
        '_JS_SUBMIT': '#saveform(sepflare_par.html)#resetToPrevious(sepflare_par.html)',
        'FLAMOD': '4',
        'ION1': '1',
        'ION2': '92',
        'ITFLARE': '0',
        'ISTART': '0',
        'FLPROB': '95.0',
        '#saveForm(sep_par.html)#namelist(sep[sep_par+magshielding_par])#RunModel(sep)#ResetToPrevious(sep_out.html)': 'Run',
        'NENERS': '75',
        'ENERFL(1)': '0.10',
        'ENERFL(2)': '0.11',
        'ENERFL(3)': '0.12',
        'ENERFL(4)': '0.14',
        'ENERFL(5)': '0.16',
        'ENERFL(6)': '0.18',
        'ENERFL(7)': '0.20',
        'ENERFL(8)': '0.22',
        'ENERFL(9)': '0.25',
        'ENERFL(10)': '0.28',
        'ENERFL(11)': '0.32',
        'ENERFL(12)': '0.35',
        'ENERFL(13)': '0.40',
        'ENERFL(14)': '0.45',
        'ENERFL(15)': '0.5',
        'ENERFL(16)': '0.55',
        'ENERFL(17)': '0.63',
        'ENERFL(18)': '0.71',
        'ENERFL(19)': '0.80',
        'ENERFL(20)': '0.90',
        'ENERFL(21)': '1.0',
        'ENERFL(22)': '1.1',
        'ENERFL(23)': '1.2',
        'ENERFL(24)': '1.4',
        'ENERFL(25)': '1.6',
        'ENERFL(26)': '1.8',
        'ENERFL(27)': '2.0',
        'ENERFL(28)': '2.2',
        'ENERFL(29)': '2.5',
        'ENERFL(30)': '2.8',
        'ENERFL(31)': '3.2',
        'ENERFL(32)': '3.5',
        'ENERFL(33)': '4.0',
        'ENERFL(34)': '4.5',
        'ENERFL(35)': '5.0',
        'ENERFL(36)': '5.5',
        'ENERFL(37)': '6.3',
        'ENERFL(38)': '7.1',
        'ENERFL(39)': '8.0',
        'ENERFL(40)': '9.0',
        'ENERFL(41)': '10.0',
        'ENERFL(42)': '11.0',
        'ENERFL(43)': '12.0',
        'ENERFL(44)': '14.0',
        'ENERFL(45)': '16.0',
        'ENERFL(46)': '18.0',
        'ENERFL(47)': '20.0',
        'ENERFL(48)': '22.0',
        'ENERFL(49)': '25.0',
        'ENERFL(50)': '28.0',
        'ENERFL(51)': '32.0',
        'ENERFL(52)': '35.0',
        'ENERFL(53)': '40.0',
        'ENERFL(54)': '45.0',
        'ENERFL(55)': '50.0',
        'ENERFL(56)': '55.0',
        'ENERFL(57)': '63.0',
        'ENERFL(58)': '71.0',
        'ENERFL(59)': '80.0',
        'ENERFL(60)': '90.0',
        'ENERFL(61)': '100.0',
        'ENERFL(62)': '110.0',
        'ENERFL(63)': '120.0',
        'ENERFL(64)': '140.0',
        'ENERFL(65)': '160.0',
        'ENERFL(66)': '180.0',
        'ENERFL(67)': '200.0',
        'ENERFL(68)': '220.0',
        'ENERFL(69)': '250.0',
        'ENERFL(70)': '280.0',
        'ENERFL(71)': '320.0',
        'ENERFL(72)': '350.0',
        'ENERFL(73)': '400.0',
        'ENERFL(74)': '450.0',
        'ENERFL(75)': '500.0'}

    do_post(url, user, password, values)

    # ('Galactic Cosmic Ray fluxes...');

    values = {
        '_JS_SUBMIT': '#saveform(gcr_par.html)#resetToPrevious(gcr_par.html)',
        'IELM': '1',
        'JELM': '92',
        'GCRMOD': '3',
        'MQ':'9677',
        '#saveForm(gcr_par.html)#namelist(gcr[gcr_par+magshielding_par])#RunModel(gcr)#ResetToPrevious(gcr_out.html)': 'Run'}

    do_post(url, user, password, values)

    # ('Ionizing dose for simple geometries...');
    values = {
        '_JS_SUBMIT': '#saveform(dose_sd.html)#resetToPrevious(dose_sd.html)',
        'JSHLD': '0',
        'DOSMOD': '2',
        'ISHLD': '3',
        'IDET': '3',
        '#saveForm(dose_sd.html)#saveForm(dose_sd.html,sd2)#namelist(sd2[dose_sd.html])#RunModel(sd2)#ResetToPrevious(sd2_out.html)': 'Run',
        'SSAT_DOSE': '0'}

    do_post(url, user, password, values)

    # OUTPUT

    # ('Save results from Ionizing dose for simple geometries...');
    string = '?%23sendResult(spenvis_s2o.txt)'
    URL = url + string
    results = requests.get(URL, auth = (user, password))
    file = open('resultsSPENVIS.txt','w')
    file.write(results.text)
    file.close()

