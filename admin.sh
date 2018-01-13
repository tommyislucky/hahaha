#! /bin/bash

while true
do
    pidof answer_BD.py # 检测程序是否运行
    while [ $? -ne 0 ]    # 判断程序上次运行是否正常结束
    do
        echo "Process exits with errors! Restarting!"
        python answer_BD.py    #重启程序
    done
    echo "Process ends!"

done
