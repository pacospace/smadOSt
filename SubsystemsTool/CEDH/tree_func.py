import numpy as np


def list_keys_values(dictionary):
    keys = []
    values = []
    for k, v in dictionary.items():
        print('key:', k, '         values:', v)
        print('')
        keys.append(k)
        values.append(v)
    return keys, values


def show_dictionary_elements(dictionary, level, graph):
    print('')
    print('')
    print('')
    print('Current Dictionary:', dictionary)
    print('')

    keys, values = list_keys_values(dictionary)
    print('all keys:', keys)
    print('number keys', len(keys))
    print('all values:', values)
    print('number values', len(values))
    print('')
    if len(keys) == len(values) and all(type(item) != type({}) for item in values):
        level += 1
        print('track n.1')
        print('The dictionary has depth: ', level)
        print('')
        print('')
        edges = len(keys)
        currentg = [level, keys, edges, values]
        graph.append(currentg)
    else:
        print('track n.2')
        level += 1
        for element in keys:
            print('')
            print('current key:', element)
            dictionaryp = dictionary[element]
            if type(dictionaryp) != type({}):
                print('track n.2.1')
                print('The dictionary has depth: ', level)
                print('')
                print('')
                edges = len(keys)
                currentg = [level, element, edges, dictionaryp]
                graph.append(currentg)
            else:
                print('track n.2.2')
                edges = len(keys)
                currentg = [level, element, edges,dictionaryp]
                graph.append(currentg)
                show_dictionary_elements(dictionaryp, level, graph)
    return graph, level


def create_nodes(graph, n_node, dot):
    nodes = []
    for node in graph[1:]:
        print('The node is: ', node)
        print('')
        if type(node[3]) != type({}):
            if type(node[1]) == type([]) and len(node[1]) > 1:
                for subnode, subvalue in zip(node[1], node[3]):
                    node_name = str(subnode).strip('[]\'') + ' : ' + str(subvalue).strip('[]\'')
                    node_ID = str(n_node)
                    print('Node ID is: ', node_ID, ' ---->  Node name is   ', node_name)
                    print('')
                    print('')
                    nodes.append([node[0], node_ID,node_name])
                    dot.node(node_ID, node_name)
                    n_node += 1
            else:
                node_name = str(node[1]).strip('[]\'') + ' : ' + str(node[3]).strip('[]\'')
                node_ID = str(n_node)
                print('Node ID is: ', node_ID, ' ---->  Node name is   ', node_name)
                print('')
                print('')
                nodes.append([node[0], node_ID, node_name])
                dot.node(node_ID, node_name)
                n_node += 1
        else:
            node_name = str(node[1]) + ' : '
            node_ID = str(n_node)
            print('Node ID is: ', node_ID, ' ---->  Node name is   ', node_name)
            print('')
            print('')
            nodes.append([node[0], node_ID, node_name])
            dot.node(node_ID, node_name)
            n_node += 1
    return nodes


def create_tree(nodes, dot):
    n_node = 0
    root_node = []
    root_node.append(nodes[0])
    for n in np.ones(len(nodes)):

        if n_node < len(nodes) - 1:
            old_node = nodes[n_node]
            current_node = nodes[n_node + 1]
            print('------------------------')
            print('Step number:', n_node)
            print('Old Node', old_node)
            print('Current Node', current_node)

            if int(current_node[0]) - int(old_node[0]) > 0:
                print('')
                print('#1 current node > old node')
                print(old_node, '--->', current_node)
                dot.edge(str(old_node[1]), str(current_node[1]))
                root_node.append(current_node)
                print('Root_node:', root_node)

            elif int(current_node[0]) - int(old_node[0]) == 0:
                print('')
                print('#2 current node = old node')
                print('Root_node:', root_node)
                root_number = (int(current_node[0])) -2
                print('Root number is:', root_number)
                print(root_node[int(root_number)], '--->', current_node)
                dot.edge(str(root_node[int(root_number)][1]), str(current_node[1]))
                root_node = root_node[0:(int(current_node[0]) - 1)]
                root_node.append(current_node)
                print('Updated root node:', root_node)

            else:
                print('')
                print('#3 current node < old node')
                diff = abs(int(current_node[0]) - int(old_node[0]))
                print('Difference of levels is:', diff)
                print('Root node:', root_node)
                print('Root_length:', len(root_node))
                s = 0
                for root in root_node:
                    if int(root[0]) == int(current_node[0]):
                        check_n = s - 1
                        break
                    s += 1
                print('Root_node position:', check_n)
                print('Root_node:', root_node[check_n][1])
                c = root_node[check_n][1]
                print(root_node[check_n], '--->', current_node)
                dot.edge(c, str(current_node[1]))

                root_node = root_node[0:check_n + 1]
                print('Check', root_node)
                root_node.append(current_node)
                print('Updated root node', root_node)
            n_node += 1

        else:
            break

    print(dot.source)
    #
    dot.render('test.gv', view=True)
