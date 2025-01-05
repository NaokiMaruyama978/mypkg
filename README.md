# ROS2 干支確認Publisher
[![test](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml)

このROS2パッケージは、現在の年から1年ずつの干支の情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`zodiac_publisher`ノードで構成されています。



## ノード概要
### `zodiac_publisher` ノード
- トピック名: `zodiac`
- 2秒ごとに以下の形式のデータをパブリッシュします:
  ```
  年:YYYY 干支:zodiac(読み)
  ```
- 現在の年から1年ずつ増加させながら、該当する干支を表示します。

## 使用方法

### 必要条件 ###
   - ROS2をインストールしてください。
## ノードの実行
### 実行コマンド
### 送り手
```
ros2 run mypkg zodiac_publisher
```
### 受け取り手
```
ros2 topic echo zodiac
```

## 実行例
以下はノードを実行した際の出力例です:

```
### - 受け取り手のログ
```
data: 年:2025 干支:巳(み)
---
data: 年:2026 干支:午(うま)
---
data: 年:2027 干支:未(ひつじ)
---
data: 年:2028 干支:申(さる)
---
data: 年:2029 干支:酉(とり)
---
data: 年:2030 干支:戌(いぬ)
```
## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアは 3条項BSDライセンス の下で再頒布および使用が許可されています。
- ©2025 Naoki Maruyama
