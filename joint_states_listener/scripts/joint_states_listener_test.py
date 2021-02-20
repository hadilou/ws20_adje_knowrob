#!/usr/bin/env python
#test client for joint_states_listener

import roslib
roslib.load_manifest('joint_states_listener')
import rospy
from joint_states_listener.srv import ReturnJointStates
import time
import sys

def call_return_joint_states(joint_names):
    rospy.wait_for_service("return_joint_states")
    try:
        s = rospy.ServiceProxy("return_joint_states", ReturnJointStates)
        resp = s(joint_names)
    except rospy.ServiceException, e:
        print "error when calling return_joint_states: %s"%e
        sys.exit(1)
    for (ind, joint_name) in enumerate(joint_names):
        if(not resp.found[ind]):
            print "joint %s not found!"%joint_name
    return (joint_name,resp.position, resp.velocity, resp.effort)


#pretty-print list to string
def pplist(list):
    return ' '.join(['%2.3f'%x for x in list])


#print out the positions, velocities, and efforts of the  arm joints
if __name__ == "__main__":
    joint_names = ["arm_1_joint",
                   "arm_2_joint",
                   "arm_3_joint",
                    "arm_4_joint",
                    "arm_7_joint",
                    "arm_5_joint",
                    "gripper_right_finger_joint"]

    while(1):
        for joint_name in joint_names:
            (name,position, velocity, effort) = call_return_joint_states([joint_name])
            print "Joint name:",name
            print "position:", pplist(position)
            print "velocity:", pplist(velocity)
            print "effort:", pplist(effort)
            time.sleep(1)
            print("---")