import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


#def cb(msg):
#    global node
#    node.get_logger().info("Listen: %d" % msg.data)

#def main():
    
    ##pub = node.create_subscription(Int16, "countup", cb, 10)
    ##rclpy.spin(node)
    
    #client = node.create_client(Query, 'query')
    #while not client.wait_for_service(timeout_sec=1.0):
    #    node.get_logger().info('待機中')

    #req = Query.Request()
    #req.name = "丸山直希"
    #future = client.call_async(req)
    #while rclpy.ok():
     #   rclpy.spin_once(node)
      #  if future.done():
       #     try:
        #        response = future.result()
         #   except:
          #      node.get_logger().info('呼び出し失敗')
           # else:
            #    node.get_logger().info("age: {}".format(response.age))

#            break

#    node.destroy_node()
 #   rclpy.shutdown()
