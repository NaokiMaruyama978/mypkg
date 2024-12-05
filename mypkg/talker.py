import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16, "countup",10)
        self.n = 0
        self.create_timer(0.5, self.cb)
    
    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)



##rclpy.init()
##node = Node("talker")
##pub = node.create_publisher(Int16, "countup", 10)
##n=0

##def cb():
##    global n
##    msg = Int16()
##    msg.data = n
##    pub.publish(msg)
##      n += 1

#def cb(request, response):
 #   if request.name == "丸山直希":
  #      response.age = 20
   # else:
    #    response.age = 255

#    return response

##def main():
##    node.create_timer(0.5, cb)
##    rclpy.spin(node)
    #srv = node.create_service(Query, "query", cb)
    #rclpy.spin(node)
