from launch.actions import ExecuteProcess
from launch import LaunchDescription
from launch_ros.actions import Node
from pathlib import Path
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    gazebo = ExecuteProcess(cmd=["gz", "sim", "-r", "chess_world.sdf"], output="screen")

    curr_pose = Node(
        package="chess_gz_wrld",
        executable="chess_tf",
    )
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
    )
    static_tf_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="static_tf_publisher",
        arguments=["0", "0", "0", "0", "0", "0", "map", "chess_board"],
        output="screen",
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
            rviz,
            static_tf_node,
        ]
    )
