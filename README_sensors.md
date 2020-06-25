# Suii Sensors
The sensors on Suii are modified to have the same specs as the real sensors.

- Lidar: Hokuyo UST-10LX
  - Detection range: 0.06 - 30m
  - Scan angle: 270°
  - Measurement steps: 1080
  - Scan speed: 25 ms (40 times/sec)

- Camera: functionality of the BlasterX Senz3D
  - 2D camera: 30 frames @ 1920x1080 - fov 77°
  - 3D Camera: 60 frames @ 640x480 - fov 85°

- Extra sensor: Sonar

### Implementation
The sensors are made and controlled in gazebo (specifically in suii_gazebo.xacro). They each use their own sensor plugins. The plugins used are as follows.

Sensor    | Sensor Type | Sensor Plugin
------    | ----------- | ------
Lidar     | gpu_ray     | libgazebo_ros_gpu_laser
Camera_2D | camera      | libgazebo_ros_camera
Camera_3D | depth       | libgazebo_ros_openni_kinect
Sonar     | ray         | libgazebo_ros_range

#### Lidar Visuals
The Lidar rays are being shown in the simulator by defualt. If one wishes to not have these visual rays they can disable them in the suii_gazebo.xacro file. In line 103 and line 136 the following line can be changed to ```true``` or ```false```:
```
<visualize>true</visualize>
```

#### Lidar not working
**!!! The Lidar needs to be able to use the graphics card. To do that you'll need to install the graphics card driver.**
To install the correct driver run the following command:
```
ubuntu-drivers devices
```
Look for the recommended driver to be installed. For example, I have the following driver:
```
vendor   : NVIDIA Corporation
driver   : nvidia-driver-440 - distro non-free recommended
 ```
 To install the driver run the following command, for me it is driver-440:
 ```
sudo apt install nvidia-driver-440
 ```
When the installation is finished, reboot your computer and now it will use your GPU.

### Sensor Topics & Messages
The sensors send their data to their specific ros topics. The rostopics that are used with the message data types are as follows:

Sensor | Topic | Msg
------ | ----- | ---
Lidar_Front | /suii/laser/scan_front  | sensor_msgs/LaserScan
Lidar_Back  | /suii/laser/scan_back   | sensor_msgs/LaserScan
Camera_2D   | /camera_2D/image_raw    | sensor_msgs/Image
Camera_3D   | /camera_3D/depth/points | sensor_msgs/PointCloud2
Sonar       | /suii/sonar/scan        | sensor_msgs/Range

_There are more topics that are being made by the sensors but aren't discussed here. They can be found, if the simulation is running, with the folliwing command._
```
rostopic list
```

### Some scripts to test the sensors:
- Move_And_Collision.py: move straight until the lidars detect a collision, then change course and stop when another collision has been detected.
- Vision_Test.py: Shows the image of the 2D camera.
