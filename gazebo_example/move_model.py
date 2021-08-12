'''
This code will move the ramp in "tt_track_carpet_ramp_pos1_trapezoid_with_smooth_multilines"
The ramp will bne move from 3 to 13 in round robin.
'''
import time
import rospy
from std_msgs.msg import Float64, Empty
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import GetLinkState, GetModelState, JointRequest, SetModelState,  SetModelStateRequest
from gazebo_msgs.msg import ModelState, ModelStates, LinkStates
from scipy.spatial.transform import Rotation
import numpy as np

TOPIC_GAZEBO_MODEL_STATE = "/gazebo/model_states"

def on_model_state_callback(message):
    #rint("callback function used!")
    #print(message)
    pass
    

# init ROS node
rospy.init_node("auto_racing", anonymous=True) 
# anonymous means ROS will give a unique id to the node if there's multiple duplication

# Wait for required services, blocking function
rospy.wait_for_service('/gazebo/get_model_state')
rospy.wait_for_service('/gazebo/set_model_state')

# ROS service 
get_model_state = rospy.ServiceProxy(
            '/gazebo/get_model_state', GetModelState)
model_state_client = rospy.ServiceProxy(
            '/gazebo/set_model_state', SetModelState)

rospy.Subscriber(TOPIC_GAZEBO_MODEL_STATE, ModelStates,
                         on_model_state_callback)

if __name__ == "__main__":

    # Get ramp position using ROS service
    model_state = get_model_state('racer', '')
    print(model_state)

    x = 1.0
    while True:
        start_quaternion = Rotation.from_euler(
            'zyx', [0, -3.14, 3.14]).as_quat()
        # Construct the model state and send to Gazebo
        model_state = ModelState()
        model_state.model_name = "ramp"
        model_state.pose.position.x = x +3
        x += 1
        if x > 10:
            x = 0
        model_state.pose.position.y = -0.8
        # prevent car bumps into the sky
        model_state.pose.position.z = 0.40
        model_state.pose.orientation.x = start_quaternion[0]
        model_state.pose.orientation.y = start_quaternion[1]
        model_state.pose.orientation.z = start_quaternion[2]
        model_state.pose.orientation.w = start_quaternion[3]
        model_state.twist.linear.x = 0
        model_state.twist.linear.y = 0
        model_state.twist.linear.z = 0
        model_state.twist.angular.x = 0
        model_state.twist.angular.y = 0
        model_state.twist.angular.z = 0
        #print(model_state)

        #req = SetModelStateRequest()
        #req.model_state =  model_state
        #res = model_state_client(req)
		#req.model_xml = xml_string
        
        # you need to call move-service for couple of dozen times to move static object in gazebo
        # it's probably a bug of Gazebo not updating static object
        for i in range(100):
            model_state_client(model_state)

        model_state = get_model_state('ramp', '')
        print("model state\n\n\n\n\n")
