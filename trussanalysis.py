import numpy
import sympy
from sympy import S, Eq, solve, symbols
import math
import pprint

class Truss():
    def __init__(self):
        self.nodes = {}
        pass

    def add_node(self, name, location, connected_nodes, support = []):
        self.nodes[name] = Node(location, connected_nodes)

    def add_load(self, node_name, magnitude):
        # this function will assume a vertical load

        self.nodes[node_name].force += magnitude
    def calculate(self):
        solve_later = []
        sol_dict = {}

        for node in self.nodes.keys():
            node_obj = self.nodes[node]
            loc = node_obj.location

            for connector_letter in node_obj.connected_nodes:
                # find the order that the force member should be placed in
                if connector_letter > node:
                    member = node + connector_letter
                elif node > connector_letter:
                    member = connector_letter + node
                else:
                    print('the nodes are equal for %s and %s this is a problem' % (node, connector_letter))

                c_loc = self.nodes[connector_letter].location

                # check if the node is directly above
                if loc[0] - c_loc[0] == 0:
                    angle = 90
                    xdist = 0
                    ydist = 'who cares'
                else:
                    xdist = abs(c_loc[0] - loc[0])
                    ydist = abs(c_loc[1] - loc[1])
                    angle = abs(math.atan(ydist/xdist))

                # find the direction that the forces are pointing
                if loc[0] < c_loc[0]:
                    x = 1
                else:
                    x = -1
                if loc[1] < c_loc[1]:
                    y = 1
                else:
                    y = -1

                print('the data for node %s (%s) compared with %s (%s) is:\nxdist: %s\nydist: %s\nangle: %s\n x: %s y:%s\nload is %s\n\n'% (node,loc, connector_letter, c_loc, xdist, ydist,angle, x,y,node_obj.force))
                f_member = symbols(member)

                if member in sol_dict.keys():
                    f_member = sol_dict[member]

                #####
                #####   WHAT YOU NEED TO DO HERE
                #####       save the direction of the x and y  equations
                #####       wait until the last pass of the connection letter and then combine
                #####       all of the equations into one equation and solve from there
                #####       then append the results into the solution dictionary
                #####

                # this code needs to  be changed here!!!!
                x_str = '%s * cos(%s) * %s' % (x, angle, member)
                y_str = '%s * sin(%s) * %s - %s' % (y,angle, member, node_obj.force)
                print('\nx_eq: %s\ny_eq: %s\n'% (x_str,y_str))
                x_eq = x * math.cos(angle) * f_member
                y_eq = y * math.sin(angle) * f_member - node_obj.force  # this assumes vertical force

                equations.append(x_eq)
                equations.append(y_eq)
        solutions = solve(equations)
        # pprint.pprint(solutions)
        print(solutions)
        return solutions



class Node():
    def __init__(self,location, nodes):
        self.location = location
        self.connected_nodes = nodes
        self.force = 0


if __name__ == '__main__':
    E = 538000 # elastic modulous of balsa wood

    t = Truss()

    # t.add_node('A', [0,0], ['B', 'C'])
    # t.add_node('B', [2,0], ['A', 'C'])
    # t.add_node('C', [1,2], ['A', 'B'])
    # t.add_load('C', 10)

    t.add_node('A', [0,2], ['B'])
    t.add_node('B', [0,0], ['A'])
    t.add_load('A', 10)

    print(t.nodes)

    t.calculate()