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
    print("---")
    
def q2():
    search = new_onto.part_of.get_relations()
    print("\n\nParts of Tiago")
    for relation in search:
        print(relation[0].name)
    print("---")

def q3():
    #Object in the scene
    search = new_onto.search(type=Object)
    print("\n\n Objects in the scene")
    for obj in search:
        print(obj.name)
    print("---")

def q4():
    #spatial reasoning
    print("Spatial locations in ontology")
    search = has_spatial_location.get_relations()
    for element in search:
        print(element)
    #single spatial location can be queried with
    print("---")
    print(cocacola.has_spatial_location)
    print(pringles.has_spatial_location)
    print("---")

def q5():
    #reachability of objects
    print("Reachability btw robot and cube: ",aruco_cube.is_reachable)
    print("Reachability btw robot and pringles: ",pringles.is_reachable)

    print("---")

def q6():
    #query performed task and goal
    print("Task afforded by:",grasp_task.is_afforded_by)
    print("Goal of the task:",grasp_task.has_goal)
    print("---")

def q7():
    #joints movements in task
    print("Joints States:")
    for state in grasp_task.has_movement:
        print(str(state))
    print("---")
    print("Example of state1:")
    print("State effort",grasp_task.has_movement[0].has_effort)
    print("State position",grasp_task.has_movement[0].has_position)
    print("State velocity",grasp_task.has_movement[0].has_velocity)
    print("State joint",grasp_task.has_movement[0].has_joint)

def q8():
    #participants of a task
    print("Participant (joints) of the task")
    for el in grasp_task.has_participant:
        print(el.name)
    print("---")
