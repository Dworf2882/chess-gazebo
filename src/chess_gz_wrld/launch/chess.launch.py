from launch.actions import ExecuteProcess
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    gazebo = ExecuteProcess(cmd=["gz", "sim", "-r", "chess_world.sdf"], output="screen")

    curr_pose = Node(
        package="chess_gz_wrld",
        executable="chess_tf",
    )

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=[
                    "ros2",
                    "run",
                    "ros_gz_bridge",
                    "parameter_bridge",
                    "/world/world_demo/pose/info@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V",
                ],
                output="screen",
            ),
            gazebo,
            curr_pose,
        ]
    )
