
from concurrent.futures import ThreadPoolExecutor
import imp
from threading import Lock
import rclpy
from rclpy.node import Node
import robot_pose_pb2
import robot_pose_pb2_grpc


import grpc

class Position(robot_pose_pb2_grpc.PositionServicer):
    
    def GetPose(self, request, context):
        print(request)
        return robot_pose_pb2.GetPoseAck



if __name__ == "__main__":
    print("Start Server...")

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
  
    robot_pose_pb2_grpc.add_PositionServicer_to_server(Position(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


