
"""
Subscribes to both camera topic (/left_image and /right_image) and creates
a grpc server from where it can be accessed.
"""
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import rclpy
from rclpy.node import Node

import grpc

class Pose(pose_pb2_grpc.PoseService):
    
    def GetPose(self, request, context):
        return pose_pb2.PoseReply



if __name__ == "__main__":
    print("Start Server...")
    opt = [('grpc.max_send_message_length', 200000), ('grpc.max_receive_message_length', 200000)]
    server = grpc.server(ThreadPoolExecutor(max_workers=10), options=opt)
    camera_pb2_grpc.add_CameraServiceServicer_to_server(CameraSDKServer(), server)
    pose_pb2_grpc.add_PoseReply_to_server(Pose(), Server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
