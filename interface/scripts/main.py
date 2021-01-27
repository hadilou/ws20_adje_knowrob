#!/usr/bin/env python3

#ontologiey related
from owlready2 import *
from get_model import *

TOP_CST = 10 # in cm
SIDE_CST = 30 #in cm

class OWLOnto():

    def __init__(self,default_path=None,path=None):
        """
        Init an ontology given its path
        """
        self.path = path
        onto_path.append(default_path)
        self.onto = get_ontology(path).load()

    def print_stats(self):
        """
        Some stats about the ontology
        """
        print("\n\n############# Some Stats about the OWL ontolology #############\n")
        print("\n\nOntology IRI:",format(self.onto.base_iri))
        print("\n\n Classes in Ontology:")
        for cls in self.onto.classes():
            print(cls)
        print("\n\nIndiduals in Ontology:")
        for indi in self.onto.individuals():
            print(indi)
        print("\n\n Object Properties of Ontology:")
        for prop in self.onto.object_properties():
            print(prop)
        print("\n\n Data Properties of Ontology:")
        for prop in self.onto.data_properties():
            print(prop)

    def assert_onto(self):
        #uses java vm
        with self.onto:
            print("/n/Starting OWL Reasoner")
            sync_reasoner()


if __name__ == '__main__':


    srdl2 = OWLOnto(r'/root/catkin_ws/src/interface/owl/',r'/root/catkin_ws/src/interface/owl/srdl2.owl')
    knowrob = OWLOnto(r'/root/catkin_ws/src/interface/owl/',r'/root/catkin_ws/src/interface/owl/knowrob.owl')
    dul = OWLOnto(r'/root/catkin_ws/src/interface/owl/',r'/root/catkin_ws/src/interface/owl/DUL.owl')
    soma = get_ontology("http://www.ease-crc.org/ont/SOMA.owl").load()
    onto = get_ontology(r'/root/catkin_ws/src/interface/owl/Tiago.owl')#,r'/root/catkin_ws/src/interface/owl/Tiago.owl')
    #tiagoOnto.print_stats()
    #tiagoOnto.assert_onto()
    #with tiagoOnto.onto:
    #   class Tiago(Thing):
    #       pass
    knowrob_namespace = onto.get_namespace("http://ias.cs.tum.edu/kb/knowrob.owl")
    soma_namespace = onto.get_namespace("http://www.ease-crc.org/ont/SOMA.owl")
    srdl2_namespace = onto.get_namespace("http://knowrob.org/kb/srdl2.owl")
    pr2_namespace = onto.get_namespace("http://ias.cs.tum.edu/kb/PR2.owl")
    dul_namespace = get_namespace("http://www.ontologydesignpatterns.org/ont/dul/DUL.owl")

    new_onto = get_ontology(r"/root/catkin_ws/src/interface/owl/new_onto.owl")
    #new_onto.load()

    #add table object to onto

    with new_onto:
        class Robot (dul_namespace.PhysicalAgent):
            pass
        class Tiago(Robot):
            pass
        class Object (dul_namespace.PhysicalObject):
            pass
        class Can (Object):
            pass
        class Table (Object):
            pass
        
        class DPose ():
            def __init__(self,x,y,z):
                self.x = float (x)
                self.y = y
                self.z = z            

        class SpatialLocation(Thing):
            pass
        class has_height(DataProperty,FunctionalProperty):
            domain = [Object]
            range = [float]
        class has_width(DataProperty,FunctionalProperty):
            domain = [Object]
            range = [float]
        class has_lenght(DataProperty,FunctionalProperty):
            domain = [Object]
            range = [float]
        class hold_pose_x(DataProperty,FunctionalProperty):
            domain = [dul_namespace.PhysicalAgent,dul_namespace.PhysicalAgent]
            range = [float]
        class hold_pose_y(DataProperty,FunctionalProperty):
            domain = [dul_namespace.PhysicalAgent,dul_namespace.PhysicalAgent]
            range = [float] 
        class hold_pose_z(DataProperty,FunctionalProperty):
            domain = [dul_namespace.PhysicalAgent,dul_namespace.PhysicalAgent]
            range = [float]
        class has_spatial_location(DataProperty,FunctionalProperty):
            domain = [dul_namespace.PhysicalAgent,dul_namespace.PhysicalAgent]
            range = [str]

    def onTop(obj1,obj2):
        ##return 1 if obj1 is on top of obj2
        # get coordinates of objects on Z axis
        # get the obj with highest z (top object)
        # check if diff on z is less than predefined value
        z1 = obj1.hold_pose_z
        z2 = obj2.hold_pose_z
        h2 = obj2.has_height
        if z1>z2:# top from bottom is z1
            if z1-z2-h2 <= TOP_CST: 
                return True
        return False
       

    def spatialSituation(obj1,obj2):
        #return the relative position(left,right) of object
        if onTop(obj1,obj2):
            return format(obj1.name) +" is on top of "+ format(obj2.name)
        elif onTop(obj2,obj1):
            return format(obj2.name) +" is on top of "+ format(obj1.name)
        elif rightTo(obj1,obj2):
            return return format(obj1.name) +" is on the right of "+ format(obj2.name)
        elif rightTo(obj2,obj1):
            return return format(obj2.name) +" is on the right of "+ format(obj1.name)
        elif leftTo(obj1,obj2):
            return return format(obj1.name) +" is on the left of "+ format(obj2.name)
        elif leftTo(obj2,obj1):
            return return format(obj2.name) +" is on the left of "+ format(obj1.name)
        else:
            return "Unkwown"

    def inside(obj1,obj2):
        #return true if object1 is inside object2
        w1 = obj1.has_width
        w2 = obj2.has_width
        h1 = obj1.has_height
        h2 = obj2.has_height
        l1 = obj1.has_lenght
        l2 = obj2.has_lenght
        x1 = obj1.hold_pose_x
        x2 = obj2.hold_pose_x
        y1 = obj1.hold_pose_y
        y2 = obj2.hold_pose_y

        if w1<w2 and h1<h2: # obj1 can be inside obj2 but it is really inside??
            if x1> x2+w2/2 and x1 < x2-w2/2: # x1 in width range ??
                if y1 > y2 + l2/2 and y1 < y2-l2/2: # y1 in lenght range?
                    return True
        return False


    def rightTo(obj1,obj2):
        # diff on x is less than threshold,
        # righter objet has bigger y
        x1 = obj1.hold_pose_x
        x2 = obj2.hold_pose_x
        y1 = obj1.hold_pose_y
        y2 = obj2.hold_pose_y

        if x1-x2 <= SIDE_CST:
            if y1 > y2 :
                return True
        return False
    
    def leftTo(obj1,obj2):
        # diff on x is less than threshold,
        # righter objet has bigger y
        x1 = obj1.hold_pose_x
        x2 = obj2.hold_pose_x
        y1 = obj1.hold_pose_y
        y2 = obj2.hold_pose_y

        if x1-x2 <= SIDE_CST:
            if y1 < y2 :
                return True
        return False

    def get_pose_of_model(gz_model_obj,model_name):
        """
        Retrieves the position of an object from Gazebo world
        """
        pose_now = gz_model_obj.get_model_pose(model_name)

        return pose_now

    def to_cm(number):
        return number*100

    tiago_1 = Tiago()
    table_1 = Table()
    can_1 = Can()

    #get pose of object , demo
    #can_1.hold_pose_x = 4
    #can_1.hold_pose_y = 5
    #can_1.hold_pose_z = 8
    #table_1.hold_pose_x = 4
    #table_1.hold_pose_y = 5
    #table_1.hold_pose_z = 3

    #from gazebo
    model_to_track_list = ["table1"]
    #gz_model_obj1 = GazeboModel(model_to_track_list)
    
    #listening to gazebo model states topic
    rospy.init_node('listener', anonymous=True)
    # coke_can_slim  kitchen_table  pringles 
    models = ["coke_can_slim","kitchen_table"]
    gz_model = GazeboModel(models)

    poses = {}
    rate = rospy.Rate(1)  # 10hz
    ready = False
    while not poses:
        for robot_name in models:
            pose_now = gz_model.get_model_pose(robot_name)
            if pose_now:
                poses[robot_name] = pose_now
                ready = True
            print ("POSE NOW ROBOT =" + robot_name + "==>" + str(pose_now))
        rate.sleep()

    if poses and ready:
        can_1.hold_pose_x = to_cm(poses["coke_can_slim"].position.x)
        can_1.hold_pose_y = to_cm(poses["coke_can_slim"].position.y)
        can_1.hold_pose_z = to_cm(poses["coke_can_slim"].position.z)
        table_1.hold_pose_x = to_cm(poses["kitchen_table"].position.x)
        table_1.hold_pose_y = to_cm(poses["kitchen_table"].position.y)
        table_1.hold_pose_z = to_cm(poses["kitchen_table"].position.z)
    
    #set lenght of objects
    table_1.has_height =  to_cm(poses["coke_can_slim"].position.z)       
    
    can_1.has_spatial_location = spatialSituation(can_1,table_1)
    print(can_1.has_spatial_location)


    
    