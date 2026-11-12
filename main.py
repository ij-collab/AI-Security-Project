import datetime
import time
now = datetime.datetime.now()
print("AI Security Monitor:", now)

import socket

host = "github.com"
port = 443

start = time.time()

try:
    with socket.create_connection((host, port), timeout=5):
        elapsed = round(time.time() - start,2)
        print("接続成功:", host)
        print("接続時間:", elapsed, "秒")
        status = "SUCCESS"
    if elapsed > 1:
        print("警告:接続速度が低下しています")
        status = "SLOW"
        status = "SUCCESS"
except OSError:
    print("接続失敗:", host)
    status = "FAILED"

with open("security.log", "a", encoding="utf-8") as f:
    f.write(f"{datetime.datetime.now()} - {host} -接続確認完了 - {status}\n")
if status == "FAILED":
    
     print("警告：接続異常を検知しました")

