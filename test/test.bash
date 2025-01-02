#!/bin/bash


dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。      

cd $dir/ros2_ws
colcon build
source $dir/.bashrc 
timeout 10 ros2 run mypkg talker | tee - /tmp/mypkg.log


cat /tmp/mypkg.log |
grep '経過時間: 00:00:10'
