# SPDX-FileCopyrightText: 2025 Naoki Maruyama
# SPDX-License-Identifier: BSD-3-Clause

import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import sys

class FilteredTrainInfoPublisher(Node):
    def __init__(self):
        super().__init__('train_info_publisher')

        # 環境変数からAPIキーを取得
        self.api_key = os.environ.get("ODPT_API_KEY")
        if not self.api_key:
            sys.exit(1)

        # パブリッシャ辞書を初期化（別名を使用）
        self.railway_publishers = {}

        # 各路線ごとのパブリッシャを設定
        self.railway_publishers["Toei.Shinjuku"] = self.create_publisher(String, 'train_info_shinjuku', 10)
        self.railway_publishers["Toei.Oedo"] = self.create_publisher(String, 'train_info_oedo', 10)
        self.railway_publishers["Toei.Asakusa"] = self.create_publisher(String, 'train_info_asakusa', 10)

        self.timer = self.create_timer(60.0, self.timer_callback)  # 60秒ごとに更新
        self.api_url = "https://api.odpt.org/api/v4/odpt:TrainInformation"
        self.target_railways = {
            "Toei.Shinjuku": "odpt.Railway:Toei.Shinjuku",
            "Toei.Oedo": "odpt.Railway:Toei.Oedo",
            "Toei.Asakusa": "odpt.Railway:Toei.Asakusa",
        }

    def timer_callback(self):
        try:
            # APIリクエストを送信
            params = {"acl:consumerKey": self.api_key}
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            train_info_list = response.json()

            # 指定した路線ごとに情報を取得
            for railway_name, railway_id in self.target_railways.items():
                for train_info in train_info_list:
                    if train_info.get("odpt:railway", "") == railway_id:
                        msg = String()
                        text = train_info.get("odpt:trainInformationText", {}).get("ja", "詳細なし")

                        # メッセージの生成とパブリッシュ
                        msg.data = f"[{railway_name}]状況:{text}"
                        self.railway_publishers[railway_name].publish(msg)
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

