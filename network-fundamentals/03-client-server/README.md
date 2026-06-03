# Client-Server 架構

## Client-Server 模型

網路上每次通訊都是 **Client（使用者端）** 主動發起請求，**Server（伺服器）** 被動回應。

> **筆記重點**
> 使用者要連到伺服器時，會在瀏覽器輸入網域名稱或 IP 位址，連線預設指向伺服器的 80 號連接埠（HTTP）；若伺服器沒有開放對應的埠，連線就無法成功。此外，當使用者只輸入網域、沒有指定任何路徑時，伺服器會自動尋找並回傳 `index.html` 作為預設首頁。

---

## DNS 解析完整流程

當你在瀏覽器輸入 `https://google.com` 並按 Enter，發生了以下事情：

```
1. 瀏覽器檢查本地 DNS 快取
   ↓（若沒有）
2. 向 ISP 的 DNS Resolver 查詢
   ↓（若不知道）
3. DNS Resolver 向 Root Server 查詢 → 回覆「.com 在那邊」
   ↓
4. 向 TLD Server 查詢 → 回覆「google.com 在那邊」
   ↓
5. 向 Authoritative Server 查詢 → 回覆「IP 是 142.250.x.x」
   ↓
6. 瀏覽器向 142.250.x.x 的 Port 443 建立 TCP 連線
   ↓
7. TLS 握手（加密）
   ↓
8. 瀏覽器發送 HTTP GET 請求
   ↓
9. 伺服器回傳 HTML
```

---

## Port Number（連接埠）

IP 帶你找到「大樓（電腦）」，Port 帶你找到「房間（程式）」。

| Port | 協定 | 說明 |
|------|------|------|
| **80** | HTTP | 沒有加密的網頁 |
| **443** | HTTPS | 加密的網頁（SSL/TLS） |
| **22** | SSH | 遠端連線伺服器 |
| **3306** | MySQL | 資料庫連線 |
| **3000 / 8080** | Dev Server | 前端開發常用 |

---

## 預設資源（Default Document）

當使用者只輸入網域（例如 `https://example.com/`），伺服器沒有指定任何路徑，
會自動回傳 `index.html`。這就是為什麼幾乎每個網站的主頁都叫 `index.html`。

---

## 前端開發實用診斷工具

| 指令 | 功能 | 使用情境 |
|------|------|---------|
| `nslookup google.com` | 查 DNS 解析結果 | 懷疑 DNS 出問題時 |
| `dig google.com` | （Mac/Linux）更詳細的 DNS 查詢 | 查看 TTL、DNS 路徑 |
| `ping 8.8.8.8` | 測試連線是否暢通 | 基本網路排錯 |
| `traceroute 8.8.8.8` | 追蹤封包路徑 | 判斷是家裡網路還是 ISP 斷了 |
| `telnet google.com 443` | 測試 Port 是否開放 | 確認伺服器端口可連 |

---

## DNS Prefetch（前端效能）

> **筆記重點**
> 在 HTML 中加入 `dns-prefetch` 提示，可以讓瀏覽器趁使用者還沒點擊連結前，就預先把目標網域的 IP 解析好。如此一來真正要連線時就能省下 DNS 查詢的那幾百毫秒等待，加快首屏載入。

```html
<link rel="dns-prefetch" href="//example.com">
```

---

## Web Accessibility 與 SEO

> **筆記重點**
> 做 SEO 時，可以透過 `<meta>` 標籤來描述頁面：在 `property` 屬性填上以 `og` 開頭的名稱（Open Graph），再依該名稱在 `content` 屬性中填入對應的關鍵字或文案，搜尋引擎與社群平台就能據此產生頁面的預覽資訊。

### 無障礙設計（Web Accessibility）

- 網頁元件可被鍵盤聚焦（Tab 鍵可到達）
- DOM 排序與視覺順序一致
- 圖片和影音標籤要標 `alt` 屬性
- 使用 ARIA 屬性（如 `aria-label`）增加可訪性

### SEO Meta 標籤

```html
<meta property="og:title" content="網站標題">
<meta property="og:description" content="網站描述">
<meta property="og:image" content="分享圖片網址">
```

這些 Open Graph（og）標籤讓搜尋引擎和社群媒體正確顯示預覽卡片。
