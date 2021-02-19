#!/usr/bin/env python
# encoding=utf-8
import datetime
import time

if __name__ == '__main__':
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("当前日期:%s" % now_str)
    timeStr = time.mktime(time.strptime(now_str, "%Y-%m-%d %H:%M:%S"))
    # 往后倒推5分钟
    timestamp = int(timeStr) * 1000 + (8 * 60 * 60 * 1000) - (1000)  # crontab调用的时候会多一秒
    print("构建时间戳:%d" % timestamp)
