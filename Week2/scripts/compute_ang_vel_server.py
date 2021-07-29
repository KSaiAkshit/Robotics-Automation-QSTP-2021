#! /usr/bin/env python3



import rospy
from std_msgs.msg import *
from week2.srv import ang_vel, ang_velResponse
from geometry_msgs import *



def compute_ang_vel_1(req):
    resp1 = ang_velResponse(0.1/req.rad)
    print(resp1)
    return resp1
    
def compute_ang_vel_server():
    rospy.init_node('compute_ang_vel_server')
    server = rospy.Service('compute_ang_vel', ang_vel, compute_ang_vel_1)
    print("ready to calc angular velocity")
    rospy.spin()

if __name__ == "__main__":
    compute_ang_vel_server()