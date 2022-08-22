
from concurrent.futures import ThreadPoolExecutor
import imp
from threading import Lock
import rclpy
from rclpy.node import Node
import robot_pose_pb2
import robot_pose_pb2_grpc


import grpc

class Pose(robot_pose_pb2_grpc.PoseServicer):
    
    def GetPose(self, request, context):
        print(request.id)
        return robot_pose_pb2.PoseReply



if __name__ == "__main__":
    print("Start Server...")

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
  
    robot_pose_pb2_grpc.add_PoseServicer_to_server(Pose(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


