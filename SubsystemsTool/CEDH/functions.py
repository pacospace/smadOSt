import xml.etree.ElementTree as ET
#retrieve the USER inputs from XML file
def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for subsystem inputs
    subsyst_inputs = []

    # iterate inputs
    inputs = tree.findall('./input')
    for input in inputs:
        model_input = input.find('model')
        name_input = input.find('name')
        value_input = input.find('value')
        subsyst_inputs.append([model_input.text, name_input.text, value_input.text])
    return subsyst_inputs

#retrieve the inputs for a specific model
def model_inputs(check,inputs):
    mod_inputs = []
    counter = 0
    for input_n in inputs:
        if inputs[counter][0] == check:
            mod_inputs.append([inputs[counter][1], inputs[counter][2]])
        counter = counter + 1
    return mod_inputs

#retrieve a specified input for a model
def specific_model_input(check,inputs):
    counter = 0
    max_value = len(inputs)
    for input in inputs:
        if counter < max_value:
            if inputs[counter][0] == check:
                input_value = inputs[counter][1]
                return input_value
                break
            else:
                counter = counter + 1
                if counter == max_value:
                    print check + ' WARNING the input requested is not available in the input file'
                    return 0