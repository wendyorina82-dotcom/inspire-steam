from pysimverse import Drone
import time

#Create an instance of drone
drone =  Drone()
drone.connect()
drone.take_off()
#distance in cm 

drone.move_forward(280)
time.sleep(1)
drone.move_backward(370)
time.sleep(1)
drone.move_left(80)
time.sleep(1)
drone.move_right(80)


time.sleep(2)

drone.land()