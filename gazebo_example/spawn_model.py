#!/usr/bin/env python

import rospy# , tf
from gazebo_msgs.srv import DeleteModel, SpawnModel, SpawnModelRequest
from geometry_msgs.msg import *

if __name__ == '__main__':
    print("Waiting for gazebo services...")
    rospy.init_node("spawn_products_in_bins")
    rospy.wait_for_service("/gazebo/delete_model")
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    print("Got it.")
    delete_model = rospy.ServiceProxy("/gazebo/delete_model", DeleteModel)
    spawn_model = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)

    with open("ramp.sdf", "r") as f:
        product_xml = f.read()

    print(product_xml)
    #orient = Quaternion(tf.transformations.quaternion_from_euler(0,0,0))
    item_pose   =   Pose(Point(x=0, y=0,    z=2),  [0, 0, 0, 1])
    object_pose = Pose()
    object_pose.position.x = 1
    object_pose.position.y = 1
    object_pose.position.z = 1
    object_pose.orientation.x = 0
    object_pose.orientation.y = 0
    object_pose.orientation.z = 0
    object_pose.orientation.w = 1
    req = SpawnModelRequest()
    req.model_name = "lul" # model name from command line input
    req.model_xml = product_xml
    req.initial_pose = object_pose
    print("Spawning model:%s", "test")
    
    #for i in range(200):
    spawn_model(req)
    '''
    for num in range(0,12):
        item_name = "product_{0}_0".format(num)
        print("Deleting model:%s", item_name)
        delete_model(item_name)

    for num in range(0,12):
        bin_y   =   2.8 *   (num    /   6)  -   1.4 
        bin_x   =   0.5 *   (num    %   6)  -   1.5
        item_name   =   "product_{0}_0".format(num)
    '''