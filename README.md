# ROS2 干支確認Publisher
[![test](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/NaokiMaruyama978/mypkg/actions/workflows/test.yml)

このROS2パッケージは、現在の年から1年ずつの干支の情報を表示する機能を持ちます。このパッケージはこれらの情報を定期的にパブリッシュする`zodiac_publisher`ノードで構成されています。

## 動作環境

このパッケージは以下の環境で動作が確認済み:
- **OS**: Ubuntu 22.04 LTS
- **ROS 2 バージョン名**: foxy

## ノード概要
### `zodiac_publisher` ノード
- トピック名: `year_zodiac`
- 2秒ごとに以下の形式のデータをパブリッシュします:
  ```
  年: YYYY, 干支: zodiac
  ```
- 現在の年から1年ずつ増加させながら、該当する干支を表示します。
