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
2\. train_info_publisher.pyの23行目のself.api_key = `"3o7usx306xa0q9chlckckk2xxm2jvthznu0vnk3fktuu9gdirfp3pzcecwlpagwa" `を取得したAPIキーに変更して下さい

### 端末1でtrain_info_publisher.pyを実行し、別の端末2でtopic確認した例
端末1
```
$ ros2 run mypkg train_info_publisher
```
端末2
```
$ ros2 topic echo train_delay_info
```
```
data: 'Lat: -14.18630938, Lon: 129.04303749, Alt: 34366.78'
---
data: 'Lat: -14.20007997, Lon: 129.04026218, Alt: 34365.72'
---
```

## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- ©2025 Naoki Maruyama
