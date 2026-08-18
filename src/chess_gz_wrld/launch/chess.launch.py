from launch.actions import ExecuteProcess
from launch import LaunchDescription


def generate_launch_description():
    gazebo = ExecuteProcess(cmd=["gz", "sim", "-r", "chess_world.sdf"], output="screen")
    chess_pieces = [
        # Белые фигуры (основные)
        "chess",
        "pawn",
        "horse",
        "idk",
        "queen",
        "king",
        "idk_b",
        "fort",
        # Черные фигуры (основные)
        "pawn_b",
        "horse_b",
        "queen_b",
        "king_b",
        "fort_b",
        # Дополнительные белые фигуры
        "horse_1",
        "fort_1",
        "pawn_1",
        "pawn_2",
        "pawn_3",
        "pawn_4",
        "pawn_5",
        "pawn_6",
        "pawn_7",
        "idk_1",
        # Дополнительные черные фигуры
        "horse_b_1",
        "fort_b_1",
        "idk_b_1",
        "pawn_b_1",
        "pawn_b_2",
        "pawn_b_3",
        "pawn_b_4",
        "pawn_b_5",
        "pawn_b_6",
        "pawn_b_7",
    ]

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
        ]
    )
