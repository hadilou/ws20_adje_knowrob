#!/usr/bin/env python3

#ontologiey related
from owlready2 import *


class Pose():
    def __init__(x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    def update(self,x=None,y=none,z=0)
        if x:self.x=x
        if y:self.y=y
        if z:self.z=z
    
    def get(self):
        return (self.x,self.y,self.z)

