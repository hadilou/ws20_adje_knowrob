#!/usr/bin/env python3

#ontologiey related
from owlready2 import *
from get_model import *

from utils import *

TOP_CST = 10 # in cm
SIDE_CST = 30 #in cm


#srdl2 = OWLOnto(r'/root/catkin_ws/src/interface/owl/',r'/root/catkin_ws/src/interface/owl/srdl2.owl')
#knowrob = OWLOnto(r'/root/catkin_ws/src/interface/owl/',r'/root/catkin_ws/src/interface/owl/knowrob.owl')
#dul = OWLOnto(r'/root/catkin_ws/src/interface/owl/',r'/root/catkin_ws/src/interface/owl/DUL.owl')
#soma = get_ontology("http://www.ease-crc.org/ont/SOMA.owl").load()
new_onto = get_ontology(r'/root/catkin_ws/src/interface/owl/Tiago.owl')#,r'/root/catkin_ws/src/interface/owl/Tiago.owl')
#tiagoOnto.print_stats()
#tiagoOnto.assert_onto()
#with tiagoOnto.onto:
#   class Tiago(Thing):
#       pass
knowrob_namespace = new_onto.get_namespace("http://ias.cs.tum.edu/kb/knowrob.owl")
soma_namespace = new_onto.get_namespace("http://www.ease-crc.org/ont/SOMA.owl")
srdl2_namespace = new_onto.get_namespace("http://knowrob.org/kb/srdl2.owl")
pr2_namespace = new_onto.get_namespace("http://ias.cs.tum.edu/kb/PR2.owl")
dul_namespace = get_namespace("http://www.ontologydesignpatterns.org/ont/dul/DUL.owl")

#new_onto = get_ontology(r"/root/catkin_ws/src/interface/owl/Tiago.owl")

#new_onto.load()

#add table object to onto

with new_onto:
    class Robot (Thing):
        def __init__(self,name):
            self.name = name
    class Tiago(Robot):
        pass
    class Object (Thing):
        pass
    class Can (Object):
        pass
    class Table (Object):
        pass
        
    class DPose (Thing):
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
        domain = [Object]
        range = [float]
    class hold_pose_y(DataProperty,FunctionalProperty):
        domain = [Object]
        range = [float] 
    class hold_pose_z(DataProperty,FunctionalProperty):
        domain = [Object]
        range = [float]
    class has_spatial_location(DataProperty,FunctionalProperty):
        domain = [Object]
        range = [str]
    #a rectangular area deliminiting a region    
    class Surface(Thing):
        def __init__(x,y,w,h):
            self.x = x #upper left x
            self.y = y #upper left y
            self.w = w #width
            self.h = h # height
    class has_grasp_region(ObjectProperty):
        domain = [Object]
        range = [DPose]

    class Grasping(Thing):pass
    class Plan(Thing):pass
    class is_plan_for(Plan >> Grasping, TransitiveProperty): pass
    class is_plan_of(Grasping >> Plan, TransitiveProperty): pass
    class has_participant(Plan >> Object, TransitiveProperty): pass
    class is_participant_of(Object >> Plan, TransitiveProperty): pass
    class is_reachable(DataProperty,FunctionalProperty):
        domain = [Object]
        range = [bool]
    class has_surface(ObjectProperty):
        domain = [Object]
        range = [Surface]   
    class is_available(DataProperty,FunctionalProperty):
        domain = [Object]
        range = [bool]
    class BodyPart(Thing): pass
    class part_of(BodyPart >> Robot, TransitiveProperty): pass
    Inverse(part_of)
    class base_link_of(Thing >> BodyPart, TransitiveProperty): pass
    class end_link_of(Thing >> BodyPart, TransitiveProperty): pass
    class Arm(BodyPart):pass 
    class Finger(BodyPart):pass
    class Gripper(BodyPart):pass 
    class LiftTorso(BodyPart):pass 
    class MobileBase(BodyPart):pass 
    class Head(BodyPart):pass 
    class Wheels(BodyPart):pass
    class has_payload(DataProperty,FunctionalProperty):
        domain = [Arm]
        range = [float]
    class has_reach(DataProperty,FunctionalProperty):
        domain = [Arm,Finger]
        range = [float]
    class has_Lift(DataProperty,FunctionalProperty):
        domain = [LiftTorso]
        range = [float]
    class has_max_speed(DataProperty,FunctionalProperty):
        domain = [LiftTorso]
        range = [float]

class SpatialReasoner():

    def onTop(self,obj1,obj2):
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

    def spatialSituation(self,obj1,obj2):
        #return the relative position(left,right) of object
        if self.onTop(obj1,obj2):
            return format(obj1.name) +" top "+ format(obj2.name)
        elif self.onTop(obj2,obj1):
            return format(obj2.name) +" top "+ format(obj1.name)
        elif self.rightTo(obj1,obj2):
            return  format(obj1.name) +" right "+ format(obj2.name)
        elif self.rightTo(obj2,obj1):
            return  format(obj2.name) +" right "+ format(obj1.name)
        elif self.leftTo(obj1,obj2):
            return  format(obj1.name) +" left "+ format(obj2.name)
        elif self.leftTo(obj2,obj1):
            return  format(obj2.name) +" left "+ format(obj1.name)
        else:
            return "Unkwown"

    def inside(self,obj1,obj2):
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


    def rightTo(self,obj1,obj2):
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
    
    def leftTo(self,obj1,obj2):
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
    
    def is_reachable(self,onto,robot: Robot,obj:Object) -> bool:
        #check if the robot can reach the object .. is robot reach >= dist(robot,object) ??
        arm = None
        reach = None
        arm = str(onto.search(is_a=new_onto.Arm,part_of=robot)[0])
        reach = onto[arm.split('.')[-1]].has_reach
        base = str(onto.search(is_a=new_onto.MobileBase,part_of=robot)[0])
        robotX = onto[base.split('.')[-1]].hold_pose_x
        robotY = onto[base.split('.')[-1]].hold_pose_y
        robotZ = onto[base.split('.')[-1]].hold_pose_z
        objectX,objectY,objectZ = obj.hold_pose_x,obj.hold_pose_y,obj.hold_pose_z
        d = distance(robotX,robotY,robotZ,objectX,objectY,objectZ)
        if d <= reach :
            return True
        return False
        


#creating instances
tiago = Tiago("tiago_1")
table = Table("table_1")
can = Can("can_1")

#parts of Tiago
tiagoArm = Arm("tiago_1_arm",part_of = [tiago],has_payload=3.0,has_reach=0.87)
tiagoGripper = Gripper("tiago_1_gripper",part_of=[tiago])
tiagoFinger_R = Finger("tiago_1_finger_R",part_of = [tiagoGripper],has_reach=0.044)
tiagoFinger_L = Finger("tiago_1_finger_L",part_of = [tiagoGripper],has_reach=0.044)
tiagoTorso = LiftTorso("tiago_1_torso",part_of = [tiago],has_lift = 0.35)
tiagoBase = MobileBase("tiago_1_base",part_of = [tiago],has_max_speed = 1)
tiagoHead = Head("tiago_1_head")
tiagoCam = BodyPart("tiago_1_cam", part_of = [tiagoHead])

#base pose

#set object properties
model_to_track_list = ["table1"]    
#listening to gazebo model states topic
rospy.init_node('listener', anonymous=True)
# coke_can_slim  kitchen_table  pringles 
models = ["coke_can_slim","kitchen_table","pringles","tiago"]
gz_model = GazeboModel(models)

poses = {}
rate = rospy.Rate(1)  # 10hz
ready = False
while not ready:
    for robot_name in models:
        pose_now = gz_model.get_model_pose(robot_name)
        if pose_now != None:
            poses[robot_name] = pose_now
        ready = len(poses) == len(models)
        print("POSE NOW ROBOT =" + robot_name + "==>" + str(pose_now))
    rate.sleep()

sr = SpatialReasoner() 

if  ready:
    can.hold_pose_x = (poses["coke_can_slim"].position.x)
    can.hold_pose_y = (poses["coke_can_slim"].position.y)
    can.hold_pose_z = (poses["coke_can_slim"].position.z)
    table.hold_pose_x = (poses["kitchen_table"].position.x)
    table.hold_pose_y = (poses["kitchen_table"].position.y)
    table.hold_pose_z = (poses["kitchen_table"].position.z)
    tiagoBase.hold_pose_x = (poses["tiago"].position.x)
    tiagoBase.hold_pose_y = (poses["tiago"].position.y)
    tiagoBase.hold_pose_z = (poses["tiago"].position.z)
    table.has_height =  (poses["coke_can_slim"].position.z)       

    ready = False
    #spatial relations
    can.has_spatial_location = sr.spatialSituation(can,table)
    table.has_spatial_location = sr.spatialSituation(table,can)
    print(can.has_spatial_location)



# auto-classify and save the ontology(only modifications made in python here are saved)
with new_onto:
    print("\n\n Starting OWL Reasoner")
    close_world(Robot)
    sync_reasoner(infer_property_values = True)
new_onto.save(file = "/root/catkin_ws/src/interface/owl/Tiago_inf.owl",format="rdfxml")










