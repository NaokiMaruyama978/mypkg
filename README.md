[![test](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml)
# mypkg
- このリポジトリは授業で作成したROS 2のパッケージです。
- このROS2パッケージは、都営浅草線・都営新宿線・都営大江戸線の現在の運行情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`train_info_publisher`ノードで構成されています。

## ノード概要
### `train_info_publisher` ノード
-  [odpt.com](https://developer.odpt.org/)のAPIを利用して、60秒ごとに都営新宿線・都営浅草線・都営大江戸線の運行情報を取得します。
- 取得した3つの路線のデータをトピックにパブリッシュします。
#### 公開されるトピック
- 公開されるトピックは以下の３つです。
  - `train_info_shinjuku`
    - 都営新宿線の運行情報
  - `train_info_oedo`
    - 都営大江戸線の運行情報
  - `train_info_asakusa`
    - 都営浅草線の運行情報
## 依存関係
このパッケージを動かすために必要なライブラリ：
- `requests`: HTTPリクエストを処理するために必要です。  
インストール方法：
```
$ pip install requests
```

## 使用方法
### 実行準備
1\. [odpt.com](https://developer.odpt.org/)でアカウントを作成し、APIキーを取得してください。   
2.環境変数を設定:  
```
$ echo "export ODPT_API_KEY='取得したAPIキー'" >> ~/.bashrc
```
```
$ source ~/.bashrc
```

### ノードの起動とデータの確認
`train_info_publisher`の実行
```
$ ros2 run mypkg train_info_publisher
```
**都営新宿線**
```
$ ros2 topic echo train_info_shinjuku
```
**都営大江戸線**
```
$ ros2 topic echo train_info_oedo
```
**都営浅草線**
```
$ ros2 topic echo train_info_asakusa
```
#### 出力例
**都営新宿線**
```
$ ros2 topic echo train_info_shinjuku
data: '[Toei.Shinjuku]状況:現在、１５分以上の遅延はありません。'
---
data: '[Toei.Shinjuku]状況:現在、１５分以上の遅延はありません。'
---
```
**都営大江戸線**
```
$ ros2 topic echo train_info_oedo
data: '[Toei.Shinjuku]状況:現在、１５分以上の遅延はありません。'
---
data: '[Toei.Shinjuku]状況:現在、１５分以上の遅延はありません。'
---
```
**都営浅草線**
```
$ ros2 topic echo train_info_asakusa
data: '[Toei.Asakusa] 状況:浅草線は、16時31分頃、三田駅にて発生した急病人救護のため、押上駅方面行列車のダイヤが乱れています。'
---
data: '[Toei.Asakusa] 状況:浅草線は、16時31分頃、三田駅にて発生した急病人救護のため、押上駅方面行列車のダイヤが乱れています。'
---
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
- 詳細は[LICENSE](https://github.com/NaokiMaruyama978/mypkg/blob/master/LICENSE)を確認してください。
- ©2025 Naoki Maruyama
