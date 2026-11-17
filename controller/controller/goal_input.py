import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class GoalInput(Node):
    def __init__(self):
        super().__init__('goal_listener')
        self.get_logger().info('goal listener started')
        
        self.publisher_ = self.create_publisher(Point, '/goal', 10)
        
def main() -> None:
    rclpy.init()
    node = GoalInput()
    try:
        while True:
            a = input("Target x y: ")
            seperated = a.split()
        
            if(len(seperated) != 2):
              print("Please enter two numbers separated by a space")
              continue
        
            try:
                x = float(seperated[0])
                y = float(seperated[1])
            except ValueError:
                print("Only numbers can be entered")
                continue
        
            msg = Point()
            msg.x = x
            msg.y = y
            node.publisher_.publish(msg)
        
    except (KeyboardInterrupt, EOFError):
        pass
    
    node.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == '__main__':
    main()