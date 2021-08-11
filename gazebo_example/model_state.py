import rospy
from std_msgs.msg import Float64, Empty
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import GetLinkState, GetModelState, JointRequest, SetModelState
from gazebo_msgs.msg import ModelState, ModelStates, LinkStates

TOPIC_GAZEBO_MODEL_STATE = "/gazebo/model_states"

def on_model_state_callback(message):
    print("callback function used!")
    print(message)

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
    model_state = get_model_state('racer', '')
    print(model_state)