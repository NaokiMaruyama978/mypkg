import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class TimeCounter(Node):
    def __init__(self):
        super().__init__('time_counter')
        self.publisher_ = self.create_publisher(String, '/time_count', 10)
        self.timer = self.create_timer(1.0, self.publish_time)  # 1秒ごとにデータを送信
        self.start_time = time.time()  # 開始時刻を記録
        self.get_logger().info("Time Counter Node started")

    def publish_time(self):
        elapsed_time = time.time() - self.start_time  # 経過時間を計算
        hours = int(elapsed_time // 3600)  # 時間
        minutes = int((elapsed_time % 3600) // 60)  # 分
        seconds = int(elapsed_time % 60)  # 秒

        # "時間:分:秒" の形式に整形
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        # メッセージを作成してパブリッシュ
        msg = String()
        msg.data = f"Elapsed time: {time_str}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"経過時間: {time_str}")

def main(args=None):
    rclpy.init(args=args)
    node = TimeCounter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

