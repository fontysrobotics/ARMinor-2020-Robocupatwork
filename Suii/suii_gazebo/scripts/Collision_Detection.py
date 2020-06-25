import rospy
from sensor_msgs.msg import LaserScan

collision_distance = 0.07
long_distance = 0.56
short_distance = 0.42


def Sensor_Front_callback(msg):
    collision_detected = False
    for i in range(len(msg.ranges)):
        if (msg.ranges[i] < collision_distance) and (msg.ranges[i] > 0):
            collision_detected = True
            print("Collision Detected! 1")
    for i in range(40, 50):
        if (msg.ranges[i] < short_distance) and (msg.ranges[i] > 0):
            collision_detected = True
            print("Collision Detected! 2")
    for i in range(15):
        if (msg.ranges[1060 + i] < long_distance) and (msg.ranges[1060 + i] > 0):
            collision_detected = True
            print("Collision Detected! 3")

    # if collision_detected:
    #     print("Collision Detected!")
    # for i in range(40, 60):
    #     print(i, msg.ranges[i])


def Sensor_Back_callback(msg):
    collision_detected = False
    for i in range(len(msg.ranges)):
        if (msg.ranges[i] < collision_distance) and (msg.ranges[i] > 0):
            collision_detected = True
            print("Collision Detected! 1")
    for i in range(20):
        if (msg.ranges[i] < short_distance) and (msg.ranges[i] > 0):
            collision_detected = True
            print("Collision Detected! 2")
    for i in range(15):
        if (msg.ranges[1060 + i] < long_distance) and (msg.ranges[1060 + i] > 0):
            collision_detected = True
            print("Collision Detected! 3")


def main():
    rospy.init_node('Collision_Detector')
    rospy.Subscriber("/suii/laser/scan_front", LaserScan, Sensor_Front_callback)
    rospy.Subscriber("/suii/laser/scan_back", LaserScan, Sensor_Back_callback)


try:
    main()
    rospy.spin()
except rospy.ROSInterruptException:
    print("Exit")
