from robodk.robolink import *       # import the robolink library (bridge with RoboDK)
RDK = Robolink()                    # establish a link with the simulator
robot = RDK.Item('ABB IRB120')      # retrieve the robot by name
robot.setJoints([0,0,0,0,0,0])      # set all robot axes to zero

target = RDK.Item('Target')         # retrieve the Target item
robot.MoveJ(target)                 # move the robot to the target

#
from robodk.robomath import *
approach