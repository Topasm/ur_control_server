
from cmath import isnan
from concurrent.futures import ThreadPoolExecutor
import imp
from threading import Lock
from urllib import request
import rclpy
from rclpy.node import Node
import robot_pose_pb2
import robot_pose_pb2_grpc
from geometry_msgs.msg import TwistStamped


import grpc


class Position(robot_pose_pb2_grpc.PositionServicer, Node):

    def __init__(self):
        super().__init__('simple_servo_twist_pub')
        self.publisher_ = self.create_publisher(TwistStamped, '/servo_node/delta_twist_cmd', 1)
    def GetPose(self, request, context):
        print(request)
        msg = TwistStamped()
        #data from unity
        #msg.header.frame_id = "tool0"
        msg.twist.linear.x = request.x
        msg.twist.linear.y = request.y
        msg.twist.linear.z = request.z
        msg.twist.angular.x = request.qx
        msg.twist.angular.y = request.qy
        msg.twist.angular.z = request.qz
       # msg.twist.orientation.w = request.qw
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
