"""
HTTP Request / Response Demo
使用 urllib 展示 GET 請求、顯示 response headers 與 status codes
"""

import urllib.request
import urllib.error
import json


def make_request(url, method='GET', data=None):
    """發送 HTTP 請求並顯示詳細資訊"""
    print(f"\n{'='*50}")
    print(f"→ {method} {url}")
    print('='*50)

    try:
        if data:
            data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=data, method=method)
            req.add_header('Content-Type', 'application/json')
        else:
            req = urllib.request.Request(url, method=method)

        req.add_header('User-Agent', 'NetworkFundamentalsDemo/1.0')

        with urllib.request.urlopen(req, timeout=5) as response:
            print(f"\n[Status] {response.status} {response.reason}")
            print("\n[Response Headers]")
            for key, val in response.headers.items():
                print(f"  {key}: {val}")

            body = response.read(200)  # 只讀前 200 bytes
            print(f"\n[Body 前 200 bytes]")
            print(f"  {body[:200]}...")

    except urllib.error.HTTPError as e:
        print(f"\n[HTTP Error] {e.code} {e.reason}")
        print(f"  → 這是 {e.code // 100}xx 錯誤：", end='')
        if e.code // 100 == 4:
            print("客戶端錯誤（請求有問題）")
        elif e.code // 100 == 5:
            print("伺服器端錯誤")

    except urllib.error.URLError as e:
        print(f"\n[URL Error] {e.reason}")
        print("  → 可能是 DNS 解析失敗或網路不通")

    except Exception as e:
        print(f"\n[Error] {e}")


def demonstrate_status_codes():
    """展示不同 HTTP status codes"""
    print("\n\n=== HTTP Status Codes 說明 ===")
    codes = [
        (200, "OK", "成功"),
        (201, "Created", "新增成功（POST 後回傳）"),
        (204, "No Content", "成功但沒有回傳內容（DELETE 常見）"),
        (301, "Moved Permanently", "永久重定向"),
        (304, "Not Modified", "瀏覽器快取有效，不需重新下載"),
        (400, "Bad Request", "請求格式錯誤（客戶端問題）"),
        (401, "Unauthorized", "需要驗證身份"),
        (403, "Forbidden", "已驗證但沒有權限"),
        (404, "Not Found", "找不到資源"),
        (500, "Internal Server Error", "伺服器內部錯誤"),
        (502, "Bad Gateway", "上游伺服器回應無效"),
        (503, "Service Unavailable", "服務暫時不可用"),
    ]
    for code, name, desc in codes:
        print(f"  {code} {name:25s} → {desc}")


def main():
    print("HTTP Request / Response Demo")
    print("對應 OSI 層：L7 應用層（Application Layer）\n")

    # 發送 GET 請求到公開 API
    make_request('https://httpbin.org/get')

    # 展示 status codes
    demonstrate_status_codes()

    # 說明
    print("\n\n=== 概念說明 ===")
    print("Request Headers 必備：")
    print("  Method: GET/POST/PUT/DELETE")
    print("  Path:   /api/users (網域後的路徑)")
    print("  Host:   api.example.com")
    print("  Cookie: session_id=abc123 (選填)")
    print()
    print("Response 必回傳：")
    print("  Status:       200 OK")
    print("  Content-Type: application/json")
    print()
    print("效能提示：")
    print("  • HTML 中的每個 <link>/<script> 都是一次 HTTP 請求")
    print("  • Minify（壓縮）CSS/JS 可減少傳輸大小")
    print("  • HTTP/2 多路復用讓多個請求共用一個 TCP 連線")


if __name__ == "__main__":
    main()
