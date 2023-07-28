#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import yagmail
import random
import time
import os
import json

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

# glados 签到 url
url = "https://glados.rocks/api/user/checkin"
cookies = {
    "koa:sess": "eyJ1c2VySWQiOjE4MzE0MSwiX2V4cGlyZSI6MTcwOTcxNzA0NDU5NiwiX21heEFnZSI6MjU5MjAwMDAwMDB9",
    "koa:sess.sig": "qXjzTrg6qFgbUcGXoRmtNvENhwU",
    "__stripe_mid": "19a75cd7-44f9-4482-8197-12d86a7a6e87d655b3"
}
# from 请求负载
value = {"token": "glados.one"}

# wait some times
time.sleep(random.randint(30, 300))

result = requests.post(url, cookies=cookies, data=value)
result_json = result.json()

print(result_json)

code = result_json['code']
message = result_json['message']

msg = {
    "status": code,
    "message": message
}

#print(msg)

# password 是 qq 的密码框(需要开启服务)
yag = yagmail.SMTP(user=email, password=password, host='smtp.qq.com')
yag.send(to=email, subject='glados sign in', contents=msg)
