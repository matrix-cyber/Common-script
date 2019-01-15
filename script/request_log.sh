#!/bin/bash

#向nginx模拟请求，每个请求更换一个用户ID，用户ID从1到20000之间的数据形的MD5值
i=0
while [ true ]; do
	#用户ID累加
	((i=$i+1))
	#将用户ID转换成MD5
	uid=`echo $i |md5sum |cut -d ' ' -f 1`

	#向nginx服务器发送请求，并带上请求头
	curl -s -o /dev/null -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36" "http://nn1.hadoop/?uid=${uid}"

	#让用户的ID在20000以内
	if [ $i -gt 20000 ]; then
		i=0
	fi

	#休息一秒发起请求
	sleep 1
done