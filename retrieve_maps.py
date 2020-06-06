"""
    
    Responsable for retrieving the graph maps that will be used to
    measure the distance between two points.

    This distance will not be geodesic, but the routing distance
    between two points.

"""

import os
import json

import networkx as nx
import osmnx as ox


def read_json(file):
    """
        Read json file with information

        Returns:
            Data dictionary
    """

    with open(file, 'rb') as json_file:

        return json.loads(json_file.read().decode('utf-8'))


def retrieve_graph_map(city_info):
    """
        Responsible for retrieving a driveble city map,
        this way it is possible to optimize routes in 
        given the real distance between points

    """

    return ox.graph_from_place("4650", network_type='drive')


def treat_city_names(city_name):

    new_names = []

    new_names.append(', '.join(city_name.values()))

    del city['State']

    new_names.append(', '.join(city_name.values()))

    del city['Country']

    new_names.append(', '.join(city_name.values()))


    return new_names



if __name__ == '__main__':


    tourism_places = read_json('Input/selected_cities.json')

    for country, cities in tourism_places.items():

        for city in cities:

            if city['City'] + '.graphml'  in os.listdir('Output'):

                continue

            if 'Bounderies' in city.keys():

                city_graph = ox.graph_from_bbox(**city['Bounderies'], network_type='drive')

            else:

                city_names = treat_city_names(city)

                city_graph = None

                for name in city_names:

                    print("Trying name: ", name)

                    try:

                        city_graph = retrieve_graph_map(name)


                        break

                    except:

                        continue

            if city_graph:

                ox.save_graphml(city_graph, filepath='Output/' + city['City'] + '.graphml')
