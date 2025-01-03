#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# タイムアウト時間を設定
timeout 20 ros2 launch mypkg zodiac_publisher.launch.py > /tmp/mypkg.log

# ログファイルの内容を検索
cat /tmp/mypkg.log | grep '年:2028,干支:申'
#cat /tmp/mypkg.log | grep '2028年の干支は申[さる]'
