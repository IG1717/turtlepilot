import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim_msgs.msg import Pose
from controller.pid import PID
from geometry_msgs.msg import Point
import math

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.get_logger().info('Turtle controller started')
        
        self.subscription = self.create_subscription(
            Point,
            '/goal',
            self.goal_callback,
            10)
        
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_period = 0.05 # 20hz 
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.x_target = None
        self.y_target = None
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.latest_pose = None
        
        self.distance_controller = PID(1,0,0)
        self.angle_controller = PID(4,0,0)
        
    def timer_callback(self):
        msg = Twist()
        if(self.latest_pose == None or self.x_target == None or self.y_target == None):
            return

        dx = self.x_target - self.latest_pose.x
        dy = self.y_target - self.latest_pose.y
        d = math.sqrt(dx**2 + dy**2)
        target_angle = math.atan2(dy, dx) 
        theta_dif = self._wrap(target_angle - self.latest_pose.theta)
        
        msg.linear.x = self.distance_controller.output(d, 0, self.timer_period)
        msg.angular.z = self.angle_controller.output(theta_dif, 0, self.timer_period)
        self.publisher_.publish(msg)
        
    def listener_callback(self, msg):
        self.latest_pose = msg
        #self.get_logger().info('I heard: "%s"' % msg._x)
        
    def goal_callback(self, msg):
        self.x_target = msg.x
        self.y_target = msg.y
        self.distance_controller.reset()
        self.angle_controller.reset()
    
    def _wrap(self, theta):
        while(theta > math.pi):
            theta = theta - 2*math.pi
        
        while(theta< -1*math.pi):
            theta = theta + 2*math.pi
        
        return theta
        
        
def main() -> None:
    rclpy.init()
    node = TurtleController()
    rclpy.spin(node)
    print('Node is spun')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()