import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.get_logger().info('Turtle controller started')
        
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
        
        
def main() -> None:
    rclpy.init()
    node = TurtleController()
    rclpy.spin(node)
    print('Node is spun')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()