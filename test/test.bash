#!/bin/bash  
# SPDX-FileCopyrightText: 2025 Naoki Maruyama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# タイムアウト時間を設定
timeout 61 ros2 launch mypkg train_info_publisher.launch.py | tee - /tmp/mypkg.log

# ログファイルの内容を検索
cat /tmp/mypkg.log | grep '[Shinjuku Line]'
cat /tmp/mypkg.log | grep '[Oedo Line]'
cat /tmp/mypkg.log | grep '[Asakusa Line]'

