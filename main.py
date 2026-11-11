import datetime

now = datetime.datetime.now()
print("AI Security Monitor:", now)

import socket

host = "github.com"
port = 443

try:
    with socket.create_connection((host, port), timeout=5):
        print("接続成功:", host)
        status = "SUCCESS"
except OSError:
    print("接続失敗:", host)
    status = "FAILED"

with open("security.log", "a", encoding="utf-8") as f:
    f.write(f"{datetime.datetime.now()} - {host} -接続確認完了 - {status}\n")
　　　if status == "FAILED":
    print("警告：接続異常を検知しました")
