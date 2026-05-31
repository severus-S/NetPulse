import os
import time
import platform
import subprocess
from datetime import datetime

# 待监控的目标服务器列表
TARGET_HOSTS = [
    {"name": "阿里云公共DNS", "host": "223.5.5.5"},
    {"name": "腾讯云公共DNS", "host": "119.29.29.29"},
    {"name": "本地网关", "host": "192.168.1.1"}
]

def ping_host(host):
    """对指定主机进行 Ping 测试，返回是否连通及延迟（毫秒）"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    
    start_time = time.time()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        end_time = time.time()
        duration = round((end_time - start_time) * 1000, 2)
        return True, duration
    except subprocess.CalledProcessError:
        return False, 0

def run_monitor():
    """主监控循环"""
    print("=" * 50)
    print(f"网络监控服务已启动: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    for target in TARGET_HOSTS:
        name = target["name"]
        host = target["host"]
        print(f"正在检查 {name} ({host})...", end="", flush=True)
        
        success, latency = ping_host(host)
        if success:
            print(f" [在线] - 延迟: {latency}ms")
        else:
            print(" [离线] - 连接失败")
    print("-" * 50)

if __name__ == "__main__":
    run_monitor()
