# ROS2 遅延情報確認Publisher
[![test](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml)

このROS2パッケージは、都営新宿線の現在の遅延情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`train_info_publisher`ノードで構成されています。



## ノード概要
### `train_info_publisher` ノード
- トピック名: `train_delay_info`
- 60秒ごとに以下の形式のデータをパブリッシュします:
  ```
  [路線] 状況:XXXX　詳細:XXXX
  ```

## 使用方法
### 実行準備
1\. [odpt.com](https://developer.odpt.org/)でアカウントを作成し、APIキーを取得してください。   
2\. fetch_posiiton.pyの17行目の`os.getenv('N2YO_API_KEY')`を取得したAPIキーに変更するか、`~/.bashrc`に`export N2YO_API_KEY='取得したAPIキー'`を追加してください。  
3\. fetch_position.pyの18行目の`25544`を取得したい衛星のNORAD IDに変更してください。

### 必要条件 ###
   - ROS2をインストールしてください。
## ノードの実行
### 実行コマンド
```
ros2 run mypkg train_info_publisher
```
## 実行例
以下はノードを実行した際の出力例です:
```
log
log
log
log
log
```
## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- ©2025 Naoki Maruyama
