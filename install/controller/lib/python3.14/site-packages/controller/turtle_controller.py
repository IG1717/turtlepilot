import rclpy
from rclpy.node import Node

class TurtleController(Node):
    def __init__(self):
        super().__init__('generic_node')
        self.get_logger().info('Turtle controller started')
        
    

def main() -> None:
    rclpy.init()
    rclpy.spin(TurtleController())
    print('Node is spun')
    


if __name__ == '__main__':
    main()