import rospy
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge
from geometry_msgs.msg import TransformStamped
import tf
import cv2

# rospy.init_node('nodename')

bridge = CvBridge()


def image_callback(msg):
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow('Camera_RGB', cv2_img)
    cv2.waitKey(10)


def depth_callback(msg):
    test = True
    # cv2_img = bridge.imgmsg_to_cv2(msg, "32FC1")
    # cv2.imshow('Camera_Depth', cv2_img)
    # cv2.waitKey(10)


def main():
    rospy.init_node('Image_Listener')
    image_topic = "/camera_2D/image_raw"
    rospy.Subscriber(image_topic, Image, image_callback)
    # depth_topic = "/camera1/depth/points"
    # rospy.Subscriber(depth_topic, PointCloud2, depth_callback)

    # rospy.Rate(10)
    #
    # transformStamped = TransformStamped()
    # transformStamped.header.stamp = rospy.Time.now()
    # transformStamped.header.frame_id = "camera"
    # transformStamped.child_frame_id = "item name"
    # transformStamped.transform.translation.x = 0    # pos_x
    # transformStamped.transform.translation.y = 0    # pos_y
    # transformStamped.transform.translation.z = 0    # pos_z
    # transformStamped.transform.rotation.x = 0       # quat_x
    # transformStamped.transform.rotation.y = 0       # quat_y
    # transformStamped.transform.rotation.z = 0       # quat_z
    # transformStamped.transform.rotation.w = 0       # quat_w
    #
    # br = tf.TransformBroadcaster()
    # br.sendTransform(transformStamped)


try:
    main()
    rospy.spin()
except rospy.ROSInterruptException:
    print("Exit")
