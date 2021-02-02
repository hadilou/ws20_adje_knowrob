#!/usr/bin/env python3
from owlready2 import *
import math

def get_pose_of_model(gz_model_obj,model_name):
    """
    Retrieves the position of an object from Gazebo world
    """
    pose_now = gz_model_obj.get_model_pose(model_name)

    return pose_now

def to_cm(number) -> float:
    return number*100


def print_stats(onto):
    """
    Some stats about the ontology
    """
    print("\n\n############# Some Stats about the OWL ontolology #############\n")
    print("\n\nOntology IRI:",format(onto.base_iri))
    print("\n\n Classes in Ontology:")
    for cls in onto.classes():
        print(cls)
    print("\n\nIndiduals in Ontology:")
    for indi in onto.individuals():
        print(indi)
    print("\n\n Object Properties of Ontology:")
    for prop in onto.object_properties():
        print(prop)
    print("\n\n Data Properties of Ontology:")
    for prop in onto.data_properties():
        print(prop)

def assert_onto(onto):
        #uses java vm
        with self.onto:
            print("/n/Starting OWL Reasoner")
            sync_reasoner()
def distance(x1,y1,z1,x2,y2,z2) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
