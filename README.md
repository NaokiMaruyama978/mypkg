[![test](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml)
# mypkg
- このリポジトリは授業で作成したROS 2のパッケージです。
- このROS2パッケージは、都営浅草線・都営新宿線・都営大江戸線の現在の遅延情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`train_info_publisher`ノードで構成されています。

## ノード概要
### `train_info_publisher` ノード
- トピック名: `train_delay_info`
- 60秒ごとに以下の形式で3つの路線の遅延データをパブリッシュします:
  ```
  [路線] 状況:XXXX　詳細:XXXX
  ```

## 使用方法
### 実行準備
1\. [odpt.com](https://developer.odpt.org/)でアカウントを作成し、APIキーを取得してください。   
2\. `train_info_publisher.py`の23行目のself.api_key = `"3o7usx306xa0q9chlckckk2xxm2jvthznu0vnk3fktuu9gdirfp3pzcecwlpagwa" `を取得したAPIキーに変更して下さい

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
data: '[Toei.Asakusa] 状況:浅草線は、16時31分頃、三田駅にて発生した急病人救護のため、押上駅方面行列車のダイヤが乱れてい ます。'
---
data: '[Toei.Shinjuku] 状況:現在、１５分以上の遅延はありません。'
---
data: '[Toei.Oedo] 状況:現在、１５分以上の遅延はありません。'
```
### テスト用コード
- test_listener.py
- train_info_publisher.launch.py

## 動作環境
このパッケージは以下の環境で動作が確認済みです。
- **OS**：Ubuntu 22.04 LTS
- **ROS2 version**：humble
  
## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- ©2025 Naoki Maruyama
