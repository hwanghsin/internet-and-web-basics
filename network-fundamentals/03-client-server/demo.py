"""
Client-Server Demo
展示簡易 HTTP Server 與 DNS 解析過程
"""

import socket
import http.server
import threading
import urllib.request
import time


def dns_resolution_demo():
    """展示 DNS 解析流程"""
    print("=== DNS 解析示範 ===\n")
    domains = ['google.com', 'github.com', 'localhost']
    for domain in domains:
        try:
            ip = socket.gethostbyname(domain)
            print(f"  {domain:20s} → {ip}")
        except socket.gaierror as e:
            print(f"  {domain:20s} → 解析失敗: {e}")

    print("\n  DNS 解析步驟：")
    print("  1. 檢查本地 /etc/hosts（localhost 就在這裡）")
    print("  2. 查瀏覽器 DNS 快取")
    print("  3. 向 ISP DNS Resolver 查詢")
    print("  4. Resolver 向 Root → TLD → Authoritative 逐層查詢")
    print("  5. 回傳 IP，瀏覽器連線到該 IP 的對應 Port\n")


def check_port(host, port, timeout=2):
    """檢查特定 Port 是否可連"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except Exception:
        return False


def port_check_demo():
    """展示 Port 檢查"""
    print("=== Port 檢查示範 ===\n")
    checks = [
        ('google.com', 80, 'HTTP'),
        ('google.com', 443, 'HTTPS'),
        ('localhost', 8080, 'Dev Server（可能未啟動）'),
    ]
    for host, port, protocol in checks:
        status = '✅ 可連' if check_port(host, port) else '❌ 不可連'
        print(f"  {host}:{port} ({protocol:25s}) → {status}")
    print()


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """簡易 HTTP 請求處理器"""

    def do_GET(self):
        print(f"\n  [Server] 收到 GET 請求：{self.path}")
        print(f"  [Server] 來自：{self.client_address[0]}")
        print(f"  [Server] Headers：{dict(self.headers)}")

        if self.path == '/':
            content = b'<h1>Hello from Python Server!</h1><p>path: /index.html</p>'
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        elif self.path == '/api/data':
            content = b'{"status": "ok", "message": "API response"}'
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
        else:
            content = b'<h1>404 Not Found</h1>'
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')

        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format, *args):
        pass  # 關閉預設 log


def start_server_demo():
    """啟動簡易伺服器並發送請求"""
    port = 7654
    server = http.server.HTTPServer(('localhost', port), SimpleHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    print(f"=== 簡易 HTTP Server（Port {port}）===\n")
    time.sleep(0.1)

    paths = ['/', '/api/data', '/unknown']
    for path in paths:
        url = f'http://localhost:{port}{path}'
        print(f"→ Client 發送 GET {url}")
        try:
            with urllib.request.urlopen(url, timeout=2) as resp:
                print(f"  ← Response: {resp.status} {resp.reason}")
                print(f"     Content-Type: {resp.headers.get('Content-Type')}")
                print(f"     Body: {resp.read()[:80].decode()}")
        except urllib.error.HTTPError as e:
            print(f"  ← Response: {e.code} {e.reason}")
        print()

    server.shutdown()


def main():
    print("Client-Server 架構 Demo")
    print("對應 OSI 層：L7 應用層（HTTP）+ L3 網路層（IP）\n")

    dns_resolution_demo()
    port_check_demo()
    start_server_demo()

    print("=== 概念說明 ===")
    print("  • Port 80  = HTTP（沒加密）")
    print("  • Port 443 = HTTPS（SSL/TLS 加密）")
    print("  • 沒有輸入路徑時，伺服器預設回傳 index.html")
    print("  • DNS prefetch 可讓瀏覽器提前解析 IP，加速連線")


if __name__ == "__main__":
    main()
