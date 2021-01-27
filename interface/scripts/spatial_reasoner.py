#!/usr/bin/env python3

#ontologiey related
from owlready2 import *

TOP_CST = 10 # in cm
SIDE_CST = 30 #in cm

def onTop(obj1,obj2):
    ##return 1 if obj1 is on top of obj2
    # get coordinates of objects on Z axis
    # get the obj with highest z (top object)
    # check if diff on z is less than predefined value
    z1 = obj1.Pose.z
    z2 = obj2.Pose.z

    if z1>z2:# top from bottom is z1
        if z1-z2 <= TOP_CST: 
            return True
    return False

def relativePos(ref,obj):
    #return the relative position(left,right) of object

def inside(obj1,obj2):
    #return true if object1 is inside object2
