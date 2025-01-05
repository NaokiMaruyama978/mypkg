import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class YearZodiacListener(Node):
    def __init__(self):
        super().__init__('year_zodiac_listener')
        self.subscription = self.create_subscription(String,'/zodiac',self.listener_callback,10)

    def listener_callback(self, msg):
        self.get_logger().info(f"受信:{msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = YearZodiacListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

