# SPDX-FileCopyrightText: 2025 Naoki Maruyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TrainInfoListener(Node):
    def __init__(self):
        super().__init__('train_info_listener')

        # トピックごとにサブスクライバを作成
        self.subscribers = {
            "Toei.Shinjuku": self.create_subscription(
                String,
                'train_info_shinjuku',
                self.shinjuku_callback,
                10
            ),
            "Toei.Oedo": self.create_subscription(
                String,
                'train_info_oedo',
                self.oedo_callback,
                10
            ),
            "Toei.Asakusa": self.create_subscription(
                String,
                'train_info_asakusa',
                self.asakusa_callback,
                10
            ),
        }

    def shinjuku_callback(self, msg):
        self.get_logger().info(f"[Shinjuku Line] Received: {msg.data}")

    def oedo_callback(self, msg):
        self.get_logger().info(f"[Oedo Line] Received: {msg.data}")

    def asakusa_callback(self, msg):
        self.get_logger().info(f"[Asakusa Line] Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    listener = TrainInfoListener()
    rclpy.spin(listener)

    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


