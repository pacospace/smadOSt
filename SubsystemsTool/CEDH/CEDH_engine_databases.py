from tree_func import show_dictionary_elements, create_nodes, create_tree, list_keys_values
from graphviz import Digraph
import numpy as np
import os.path
from collections import defaultdict


def CRUD_operation_request():
    print('''Engine_database:  
        - INSERT element to DB:    1
        - READ from DB:            2
        - UPDATE element from DB:  3
        - DELETE element from DB:  4 
        - To close the DB:         esc ''')
    operation = input('Select the action you want to take (e.g. the number): ')
    return operation


def crud_operations(operation):

    while operation != 'esc':

        if operation == '1':

            if os.path.exists('db_components.npy') is False:
                dictionary = {}
                np.save('db_components.npy', dictionary)
            else:
                dictionary = np.load('db_components.npy').item()

            if dictionary == {}:
                print('Create new DB:')
                print('Insert name:')
                new_DB_name = str(input())
                if type(new_DB_name) != type('t'):
                    new_DB_name = str(input())

                else:
                    dictionary[new_DB_name] = {}

            print(dictionary)
            keys, values = list_keys_values(dictionary)
            print(keys)
            new_DB_name = str(keys).strip('[]\'')

            graphds, level = show_dictionary_elements(dictionary, 0, [[0, 0, 0, 0]])
            print('The tree has depth: ', level)
            for element in graphds[1:]:  # excluding initial point
                print(element)

            dot = Digraph(comment='CEDH components')
            nodes = create_nodes(graphds, 0, dot)
            for node in nodes:
                print(node)
            create_tree(nodes, dot)

            print('Insert name of the component')
            name = str(input())
            nameID = str('ID_' + name)
            dictionary[new_DB_name][nameID] = {}

            data_component = ['Class', 'Type', 'Company', 'Mass_kg', 'Cost_euro', 'Power_W', 'Volume_x_cm2', 'Volume_y_cm2',
                              'Volume_z_cm2']
            data_comments = ['''
                                Class

                                1: Commercial
                                2: Cubesat tech
                                3: ESA legacy
                                4: New space technologies
                            ''',
                            ''' Type of OBC
                            
                                1: OBC 
                                2: OBC + TM/TC 
                                3: OBC + Mass Memory 
                                4: OBC + Mass memory + Casing&Internal harness
                                5: OBC + TM/TC + Mass memory + Casing&Internal harness
                                6: OBC + TM/TC + Mass memory + Casing&Internal harness + Power''',
                             '',
                             '',
                             '',
                             '',
                             '',
                             '',
                             '']

            for data, comment in zip(data_component, data_comments):

                print('')
                print('INSERT ', data)
                print('''
                
                ''', comment, '''
                
                ''')

                s_data = str(input())

                dictionary[new_DB_name][nameID][str(data)] = s_data

            np.save('db_components.npy', dictionary)

            operation = CRUD_operation_request()

        elif operation == '2':

            dictionary = np.load('db_components.npy').item()

            print(dictionary)

            if dictionary == {}:
                print('the dictionary is empty')
            else:
                print('READ component in the DB')

                graphds, level = show_dictionary_elements(dictionary, 0, [[0, 0, 0, 0]])
                print('The tree has depth: ', level)
                for element in graphds[1:]:  # excluding initial point
                    print(element)

                dot = Digraph(comment='CEDH components')
                nodes = create_nodes(graphds, 0, dot)
                for node in nodes:
                    print(node)
                create_tree(nodes, dot)

            operation = CRUD_operation_request()

        elif operation == '3':
            print('UPDATE element in the DB')
            print('\nWARNING!!!!!  This function has not been implemented yet!!!!\n')
            operation = CRUD_operation_request()

        elif operation == '4':
            print('DELETE element from DB')

            dictionary = {}
            np.save('db_components.npy', dictionary)

            operation = CRUD_operation_request()

        else:
            operation = CRUD_operation_request()
            return crud_operations(operation)


def main():
    nested_dict = lambda: defaultdict(nested_dict)
    dictionary = nested_dict()
    operation = CRUD_operation_request()

    crud_operations(operation)


if __name__ == '__main__':
    main()
