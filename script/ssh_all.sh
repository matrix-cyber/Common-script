#！ /bin/bash
#做一个多级操作脚本，执行该脚本，来操作多台机器

#获取当前脚本所在位置
cd `dirname $0`

#获取路径
path=`pwd`

#查看文件内容
ip_arr=`cat "${path}/ips"`

#以数组的形式进行遍历
for ip in ${ip_arr[*]}
do
    #拼接ssh命令，格式： ssh 用户名@主机名  操作
    cmd="ssh luser@${ip} $*"
    echo $cmd

    #动态执行
    if eval $cmd ; then
        echo "ok"
    else
        echo "fail"
    fi
done