#!/bin/bash

#获取执行路径
RUN_HOME=$(cd "$(dirname "$0")"; echo "${PWD}")

#查看hosts文件内容
NOW_LIST=(`cat ${RUN_HOME}/ips`)

#以数组的形式进行遍历
SSH_USER="hadoop"
for i in ${NOW_LIST[@]};do
    #拼接ssh命令，格式： ssh 用户名@主机名  操作
    cmd="ssh $SSH_USER@$i \"$*\""
    echo $cmd

    #动态执行
    if eval $cmd ; then
        echo "OK"
    else
        echo "FAIL"
    fi
done
