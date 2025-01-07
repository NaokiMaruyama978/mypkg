#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Naoki Maruyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TrainInfoListener(Node):
    def __init__(self):
        super().__init__('train_info_listener')
        self.subscription = self.create_subscription(
            String,
            'train_delay_info',  
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Train Info Listener has started.')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    listener = TrainInfoListener()
    rclpy.spin(listener)

    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


