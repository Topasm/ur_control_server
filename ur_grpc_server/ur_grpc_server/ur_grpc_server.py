
from cmath import isnan
from concurrent.futures import ThreadPoolExecutor
import imp
from threading import Lock
from urllib import request
import rclpy
from rclpy.node import Node
import robot_pose_pb2
import robot_pose_pb2_grpc
from geometry_msgs.msg import PoseStamped


import grpc


class Position(robot_pose_pb2_grpc.PositionServicer, Node):

    def __init__(self):
        super().__init__('simple_servo_twist_pub')
        self.publisher_ = self.create_publisher(PoseStamped, '/target_pose', 1)
    def GetPose(self, request, context):
        print(request)
        msg = PoseStamped()
        #data from unity
        msg.header.frame_id = "wrist_3_link"
        msg.pose.position.x = request.x
        msg.pose.position.y = request.y
        msg.pose.position.z = request.z +0.5
        msg.pose.orientation.x = request.qx
        msg.pose.orientation.y = request.qy
        msg.pose.orientation.z = request.qz
        msg.pose.orientation.w = request.qw
        self.publisher_.publish(msg)
        # print(request)
        return robot_pose_pb2.GetPoseAck




    
  



if __name__ == "__main__":
    print("Start Server...")


    rclpy.init(args=None)

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
  
    robot_pose_pb2_grpc.add_PositionServicer_to_server(Position(), server)

    
    server.add_insecure_port('[::]:50051')
    server.start()
   


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    server.wait_for_termination()

    rclpy.shutdown()
