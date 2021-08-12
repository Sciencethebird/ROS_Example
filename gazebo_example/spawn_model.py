'''
Modyfied from https://github.com/ipa320/srs_public/blob/master/srs_user_tests/ros/scripts/spawn_object.py
This Code will delete original ramp in "tt_track_carpet_ramp_pos1_trapezoid_with_smooth_multilines"
and spawn a new ramp with name "lul"
'''
import time
import rospy
from gazebo_msgs.srv import DeleteModel, SpawnModel, DeleteModelRequest, SpawnModelRequest
from geometry_msgs.msg import *

if __name__ == '__main__':

    # ROS node init
    rospy.init_node("spawn_products_in_bins")

    '''
    Model Spawning 
    '''

    # ROS spawning service
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)

    # Model Spawning
    with open("ramp.sdf", "r") as f:
        object_xml = f.read()
    print(object_xml)

    object_pose = Pose()
    object_pose.position.x = 1
    object_pose.position.y = 1
    object_pose.position.z = 1
    object_pose.orientation.x = 0
    object_pose.orientation.y = 0
    object_pose.orientation.z = 0
    object_pose.orientation.w = 1

    req = SpawnModelRequest()
    name = "lul"
    req.model_name = name # name of your model in Gazebo
    req.model_xml = object_xml
    req.initial_pose = object_pose
    print(f"Spawning model: {name}")
    
    res = spawn_model(req)
    # evaluate response
    if res.success == True:
    	rospy.loginfo(res.status_message + " " + name)
    else:
    	print (f"Error: model {name} not spawn. error message = {res.status_message}")

    
    # Temp Stop
    time.sleep(5)


    '''
    Model Deleting
    '''
    # Model Deleting Service
    rospy.wait_for_service("/gazebo/delete_model")
    delete_model = rospy.ServiceProxy("/gazebo/delete_model", DeleteModel)
    srv_delete_model = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)

    name = "ramp"
    req = DeleteModelRequest()
    req.model_name = name
    res = srv_delete_model(name)
    if res.success == True:
        rospy.loginfo(f"Model '{name}' successfully deleted")
    else:
        rospy.loginfo(f"Model '{name}' does not exist in gazebo.")
        
        


