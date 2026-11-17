import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim_msgs.msg import Pose

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.get_logger().info('Turtle controller started')
        
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg._x)
        
        
def main() -> None:
    rclpy.init()
    node = TurtleController()
    rclpy.spin(node)
    print('Node is spun')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()