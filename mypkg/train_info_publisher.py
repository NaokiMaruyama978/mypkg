#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Naoki Maruyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import sys

class FilteredTrainInfoPublisher(Node):
    def __init__(self):
        super().__init__('filtered_train_info_publisher')
        self.publisher_ = self.create_publisher(String, 'train_delay_info', 10)
        self.timer = self.create_timer(60.0, self.timer_callback)  # 60秒ごとに更新
        self.api_url = "https://api.odpt.org/api/v4/odpt:TrainInformation"
        self.api_key = "3o7usx306xa0q9chlckckk2xxm2jvthznu0vnk3fktuu9gdirfp3pzcecwlpagwa"  # 取得したAPIキーを設定 
        self.target_railways = [
 
            "odpt.Railway:Toei.Shinjuku", 
                ] 
        #self.get_logger().info('Filtered Train Info Publisher has started.')

    def timer_callback(self):
        try:
            # APIリクエストを送信
            params = {"acl:consumerKey": self.api_key}
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            train_info_list = response.json()

            # 指定した路線の情報をフィルタリング
            for train_info in train_info_list:
                railway = train_info.get("odpt:railway", "")
                if railway in self.target_railways:
                    msg = String()
                    status = train_info.get("odpt:trainInformationStatus", "情報なし")
                    text = train_info.get("odpt:trainInformationText", {}).get("ja", "詳細なし")
                    
                    railway_name = railway.replace("odpt.Railway:", "")
                    msg.data = f"[{railway_name}] 状況:{text} 詳細:{status}"
                    self.publisher_.publish(msg)
                    #self.get_logger().info(f'Published: {msg.data}')
        except Exception as e:
            sys.exit(1)


def main(args=None):
    rclpy.init(args=args)
    publisher = FilteredTrainInfoPublisher()
    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
