# SPDX-FileCopyrightText: 2025 Naoki Maruyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class YearZodiacPublisher(Node):
    def __init__(self):
        super().__init__('year_zodiac_publisher')
        self.publisher_ = self.create_publisher(String, '/zodiac', 10)
        self.timer = self.create_timer(2.0, self.publish_year_zodiac)  # 2秒ごとに更新
        self.year = 2025  # 初期年を2025年に設定
        #self.get_logger().info("Year and Zodiac Publisher Node started")

    def get_zodiac(self, year):
        # 干支を計算（2025年を基準として）
        zodiacs = ['辰', '巳', '午', '未', '申', '酉', '戌', '亥','子', '丑', '寅', '卯']
        zodiacs_yomi = ['たつ','み','うま','ひつじ','さる','とり','いぬ','い','ね','うし','とら','う']
        index = (year - 2024) % 12
        return zodiacs[index],zodiacs_yomi[index]

    def publish_year_zodiac(self):
        # 現在の年と対応する干支を取得
        zodiac, zodiacs_yomi = self.get_zodiac(self.year)
        message = f"年:{self.year} 干支:{zodiac}({zodiacs_yomi})"
        
        # メッセージを作成して送信
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)

        # ログに送信した内容を表示
        self.get_logger().info(f" {msg.data}")

        # 年を1年増やす
        self.year += 1

def main(args=None):
    rclpy.init(args=args)
    node = YearZodiacPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
