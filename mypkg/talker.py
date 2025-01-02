import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import requests

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, '/gps_data', 10)
        self.timer = self.create_timer(2.0, self.publish_gps_data)  # 1秒ごとにデータを送信
        self.get_logger().info("GPS Publisher Node started")

    def get_ip_location(self):
        # IPアドレスから位置情報を取得するAPIを利用
        response = requests.get('https://ipinfo.io')
        data = response.json()
        
        # 緯度と経度を抽出
        location = data['loc'].split(',')
        latitude = float(location[0])  # 緯度
        longitude = float(location[1])  # 経度
        #self.get_logger().info(f"IP Location: Latitude: {latitude}, Longitude: {longitude}") 
        return latitude, longitude

    def publish_gps_data(self):
        # IPアドレスから位置情報を取得
        latitude, longitude = self.get_ip_location()

        # NavSatFixメッセージを作成
        gps_msg = NavSatFix()
        gps_msg.latitude = latitude
        gps_msg.longitude = longitude
        gps_msg.altitude = 10.0  # 仮の高度 (10メートル)
        
        # 仮の精度情報
        gps_msg.position_covariance = [0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5]
        gps_msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
        
        # メッセージを送信
        self.publisher_.publish(gps_msg)
        
        # ログに送信した内容を表示
        self.get_logger().info(f"Published GPS: 緯度: {gps_msg.latitude:.6f}, 経度: {gps_msg.longitude:.6f}, 高度: {gps_msg.altitude:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = GPSPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

