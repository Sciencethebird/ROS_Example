import time
import rospy
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
    req.model_name = "lul" # name of your model in Gazebo
    req.model_xml = object_xml
    req.initial_pose = object_pose
    print(f"Spawning model: {req.model_name}")
    
    spawn_model(req)

    time.sleep(5)

    # deleting model
    

