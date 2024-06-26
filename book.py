#!/usr/bin/env python
# coding=utf-8
'''
Author       : taooooo 791545998@qq.com
Date         : 2024-05-16 22:45:57
LastEditors  : taooooo 791545998@qq.com
LastEditTime : 2024-06-10 22:04:28
Description  : 

'''

import requests
import json
import time
import threading
from datetime import datetime, timedelta

# 请将date_string、week替换为实际的值
date_string = "2024-06-17"
week = 1
# 请将start_time和end_time替换为实际的时间段
# start_time = "12:00"
# end_time = "13:00"
# 多个时间段
time_slots = [("12:00", "13:00"), ("13:00", "14:00")]  
# 请将venue_id替换为实际的场地ID
# venue_id = 8
# 请将Authorization替换为实际的token
Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJhNWM5ZjkwMi1hZGNlLTQzZmMtOGU4Ny00NjlmOGFkNWYxYjUiLCJpYXQiOjE3MTc1OTYxNTgsImV4cCI6MTcxNzY4MjU1OCwidXNlckluZm8iOnsidXNlclJvbGVJZCI6MSwiYWNjb3VudCI6IjIwMjIyMTAxNzc5OCIsInNubyI6IjIwMjIyMTAxNzc5OCJ9LCJzZXgiOjEsInVzZXJJZCI6MjU5MjM0NTA1NzgzMzcsInNlcmlhbFZlcnNpb25VSUQiOi03NzAwODI1OTA0ODMwNzA0NjE5LCJpc0luaXRQYXNzd29yZCI6ZmFsc2UsInBob25lIjoiJHNpZ246cTl4djNBME4zMmtESkQyVVhueHlYZz09Iiwibmlja25hbWUiOiLljY7mhYjmtpsiLCJ0YWciOiJtaW5pIiwiaXNSZWFsTmFtZSI6dHJ1ZSwiYWNjb3VudCI6IiRzaWduOk1BN1krcFhGR0JDeEZaSlFKalNmQUE9PSJ9.Ml7ow_fafaJD5WfeEcWsmP4a9HyCXW1INiNUOHsvxA2Exoy8MYqqQuWraBanP4y3mf4d5s_nUKOSygujXlpnO7GTyuBbfx3_TTVB20xAxr4IKAdU1VaWOuxHNx_A9qqF5NbQM1LjXk-FLQVoJH0ipdDMq02WjSjl7-5Ai-W4wtQElxXa4qK3PjYT7EbOQU3L0-xOY7uP1SSf8T4a8cuSFPJZRxx-Rs0bga3eNtXR36R8LzJ12kwV6JfsV3o43CAXo2m_78fI6lbzlUQh7KU-T2RcDwtxzFLfzO1fRKDArBrRmlHf6BGfT7Xybpxf_ZSfVNZg0jUExZc0cNcny9KpkQ"
# 停止信号
should_stop = False

# 场地的venueId
venue_ids = {
    1: 511508061201884,
    2: 511589859434885,
    5: 511839951512888,
    6: 511942956511889,
    7: 512037093039890,
    8: 512160523250891,
    9: 512288707374892,
    10: 512382636613893,
    11: 51246724428894,
    12: 512536644146895
}

# 请求头
headers = {
    "Connection": "keep-alive",
    "xweb_xhr": "1",
    "Authorization": Authorization,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wxe4bbc47ea32ad29f/6/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

# 计算belongDate的函数
def calculate_belong_date(days_in_future):
    future_date = datetime.now() + timedelta(days=days_in_future)
    return int(future_date.timestamp() * 1000)

def get_belong_date(date_string):
    # 将日期字符串转换为datetime对象
    date = datetime.strptime(date_string, "%Y-%m-%d")

    # 将datetime对象转换为时间戳（以毫秒为单位）
    timestamp = int(date.timestamp() * 1000)

    return timestamp



def book_venue(start_time, end_time):
    while not should_stop:
        for venue_id in venue_ids.keys():
            # 请求体
            payload = {
                "receipts": 0,
                "mode": "week",
                "buyerSource": 1,
                "stadiumId": 1,
                "rentals": [
                    {
                        "venueId": venue_ids[venue_id],  # 替换为实际的场地ID
                        "belongDate": get_belong_date(date_string),  # 替换为实际的日期时间戳
                        "week": week,
                        "start": start_time,
                        "end": end_time
                    }
                ]
            }

            # 发送POST请求，关闭SSL证书验证
            response = requests.post("https://venue.spe.scut.edu.cn/api/mini/order/rental/orders/apply", headers=headers, data=json.dumps(payload), verify=False)
            response_data = json.loads(response.text)
           
            # 如果请求成功，打印响应并退出循环
            if response_data["code"] == 1:
                print("预定成功！")
                print(response.text)
                return
            else:
                print("预定失败，正在重试...")
                print(response.text)

            # 等待0.1秒后再次尝试
            time.sleep(0.05)
        time.sleep(0.2)

def threads_join(threads):
    '''
    令主线程阻塞,等待子线程执行完才继续,使用这个方法比使用join的好处是,可以ctrl+c kill掉进程
    '''
    for t in threads:
        while 1:
            if t.isAlive():
                time.sleep(10)
            else:
                break

def wait_until(target_time: datetime):
    """等待直到目标时间"""
    now = datetime.now()
    wait_seconds = (target_time - now).total_seconds()
    if wait_seconds > 0:
        time.sleep(wait_seconds)


if __name__ == "__main__":

    target_time = datetime.now().replace(hour=23, minute=59, second=35, microsecond=0)
    wait_until(target_time)

    # 创建线程列表
    threads = []

    # 为每个时间段创建一个新的线程
    for start_time, end_time in time_slots:
        thread = threading.Thread(target=book_venue, args=(start_time, end_time))
        thread.setDaemon(True)
        threads.append(thread)

    # 启动所有线程
    for thread in threads:
        thread.start()

    time.sleep(40)
    should_stop = True  # 通知线程停止

    # 等待所有线程完成
    # threads_join(threads)
    for thread in threads:
        thread.join()