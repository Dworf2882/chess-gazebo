# WARNING:
# /world/world_demo/pose/info
# tf2_msgs/msg/TFMessage
# chess_pieces = [
#     "chess",
#     "pawn",
#     "horse",
#     "idk",
#     "queen",
#     "king",
#     "idk_b",
#     "fort",
#     "pawn_b",
#     "horse_b",
#     "queen_b",
#     "king_b",
#     "fort_b",
#     "horse_1",
#     "fort_1",
#     "pawn_1",
#     "pawn_2",
#     "pawn_3",
#     "pawn_4",
#     "pawn_5",
#     "pawn_6",
#     "pawn_7",
#     "idk_1",
#     "horse_b_1",
#     "fort_b_1",
#     "idk_b_1",
#     "pawn_b_1",
#     "pawn_b_2",
#     "pawn_b_3",
#     "pawn_b_4",
#     "pawn_b_5",
#     "pawn_b_6",
#     "pawn_b_7",
# ]


from tf2_msgs.msg import TFMessage
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import numpy as np
import math
import rclpy
from rclpy.node import Node


def mathshit():
    pass


class FramePublisher(Node):
    def __init__(self):
        super().__init__("chess_frame_pub")
        self.tf_broadcaster = TransformBroadcaster(self)
        self.chess_pieces = [
            "chess",
            "pawn",
            "horse",
            "idk",
            "queen",
            "king",
            "idk_b",
            "fort",
            "pawn_b",
            "horse_b",
            "queen_b",
            "king_b",
            "fort_b",
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

        self.subscription = self.create_subscription(
            TFMessage, f"/world/world_demo/pose/info", self.chess_transformation_pub, 1
        )
        self.subscription

    def chess_transformation_pub(self, msg):

        for tfs in msg.transforms:
            if tfs.child_frame_id in self.chess_pieces:
                t = TransformStamped()
                t.header.stamp = self.get_clock().now().to_msg()

                t.header.frame_id = "chess_board"
                t.child_frame_id = tfs.child_frame_id
                pose = tfs.transform
                t.transform.translation.x = pose.translation.x
                t.transform.translation.y = pose.translation.y
                t.transform.translation.z = pose.translation.z

                t.transform.rotation.x = pose.rotation.x
                t.transform.rotation.y = pose.rotation.y
                t.transform.rotation.z = pose.rotation.z
                t.transform.rotation.w = pose.rotation.w

                # Send the transformation
                self.tf_broadcaster.sendTransform(t)


def main():
    rclpy.init()
    node = FramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
