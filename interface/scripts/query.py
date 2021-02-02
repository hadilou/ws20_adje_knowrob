#!/usr/bin/env python3

#ontologiey related
from owlready2 import *
from utils import *
from onto import SpatialReasoner as sr
from onto import *
#import inferred ontology
#new_onto = get_ontology(r'/root/catkin_ws/src/interface/owl/Tiago_inf.owl').load()
#print stats of ontology


def q1():
    print_stats(new_onto)
    #Part of Tiago
    
def q2():
    search = new_onto.part_of.get_relations()
    print("\n\nParts of Tiago")
    for relation in search:
        print(relation[0])
    
def q3():
    #Object in the scene
    search = new_onto.search(type=Object)
    print("\n\n Objects in the scene")
    print(search)

def q4():
    #spatial reasoning
    print("Spatial locations in ontology")
    search = has_spatial_location.get_relations()
    for element in search:
        print(element)
    #single spatial location can be queried with
    print(can.has_spatial_location)

def q5():
    #reachability of objects
    print("Reachability btw robot and table: ",sr.is_reachable(new_onto,tiago,table))


