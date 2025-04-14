import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/skafee/Documents/cours/framework_robotique/ros2_gazebo/tp_ws/install/gazebo_perso'
