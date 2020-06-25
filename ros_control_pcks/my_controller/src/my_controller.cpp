
#include <controller_interface/controller.h>
#include <hardware_interface/joint_command_interface.h>
#include <pluginlib/class_list_macros.h>
#include <std_msgs/Float64.h>
namespace my_controller_ns
{
class MyPositionController :public controller_interface::Controller<hardware_interface::EffortJointInterface>
}
