"""
IP 定址 Demo
展示本機 IP 查詢、DNS 解析等基本 socket 操作
"""

import socket
import subprocess
import sys


def get_local_ip():
    """取得本機在區域網路的私有 IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"無法取得: {e}"


def dns_lookup(hostname):
    """將網域名稱解析為 IP（模擬 DNS 查詢）"""
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror as e:
        return f"DNS 解析失敗: {e}"


def reverse_dns(ip):
    """反向 DNS：從 IP 查詢主機名稱"""
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "無對應主機名稱"


def check_ip_type(ip):
    """判斷 IP 是私有還是公有"""
    parts = list(map(int, ip.split(".")))
    if (
        parts[0] == 10
        or (parts[0] == 172 and 16 <= parts[1] <= 31)
        or (parts[0] == 192 and parts[1] == 168)
        or ip.startswith("127.")
    ):
        return "私有 IP（Private IP）"
    elif ip.startswith("169.254."):
        return "⚠️  APIPA（DHCP 失敗，無法連網）"
    else:
        return "公有 IP（Public IP）"


def main():
    print("=" * 50)
    print("IP 定址 Demo")
    print("=" * 50)

    # 本機資訊
    hostname = socket.gethostname()
    local_ip = get_local_ip()
    print(f"\n本機主機名稱: {hostname}")
    print(f"本機私有 IP:  {local_ip}")
    print(f"IP 類型:      {check_ip_type(local_ip)}")

    # Loopback
    print(f"\nLoopback 位址: 127.0.0.1（localhost）")
    print(f"  → 永遠指向自己，不需要網路連線")

    # DNS 解析
    print("\n--- DNS 解析範例 ---")
    domains = ["google.com", "github.com"]
    for domain in domains:
        ip = dns_lookup(domain)
        print(f"  {domain:20s} → {ip}")

    # IP 類型判斷
    print("\n--- IP 類型判斷 ---")
    test_ips = ["192.168.1.1", "10.0.0.1", "8.8.8.8", "169.254.1.1", "127.0.0.1"]
    for ip in test_ips:
        print(f"  {ip:15s} → {check_ip_type(ip)}")

    # 概念說明
    print("\n--- 概念對應 ---")
    print("  LAN（區域網路）：同一 Wi-Fi 下的設備都在同個子網路")
    print("  WAN（廣域網路）：透過 ISP 連接到公有 IP 的世界")
    print("  NAT：路由器讓多台私有 IP 設備共用一個公有 IP")
    print()


if __name__ == "__main__":
    main()
