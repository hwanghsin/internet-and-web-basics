# OSI 七層模型（OSI 7-Layer Model）

## 什麼是 OSI 模型？

OSI（Open Systems Interconnection）模型是網路界的「憲法」，
定義了資料從應用程式到實體線路的路徑，確保不同廠牌設備能互相溝通。

> **筆記重點**
> 試想，如果沒有一套共通標準，不同廠牌、不同作業系統的設備就可能彼此「聽不懂對方在說什麼」。OSI 模型正是為了解決這個問題而制定的全球標準，讓各家設備都能依循同一套規則順利溝通。

---

## 七層模型詳解（由上到下）

| 層級 | 名稱 | 處理單位 | 核心功能 | 關鍵協定/設備 |
|------|------|---------|---------|-------------|
| **L7** | 應用層 Application | Data | 使用者介面與應用程式互動 | HTTP, FTP, SMTP, DNS |
| **L6** | 展示層 Presentation | Data | 翻譯、加密、壓縮 | SSL/TLS, UTF-8, JPEG |
| **L5** | 會話層 Session | Data | 建立、管理、終止連線 | Session, Cookie |
| **L4** | 傳輸層 Transport | Segment | 端對端可靠傳輸（Port） | TCP, UDP |
| **L3** | 網路層 Network | Packet | 路由決策（IP 位址） | IP, ICMP / Router |
| **L2** | 資料連結層 Data Link | Frame | 區域網路點對點傳輸 | Ethernet, MAC / Switch |
| **L1** | 實體層 Physical | Bit | 0 與 1 的電子訊號 | 網路線, Wi-Fi, 光纖 |

---

## 封裝（Encapsulation）：俄羅斯娃娃

資料發送時，從 L7 向下，每一層都**套上一個「信封」（Header）**，這叫封裝。
接收端從 L1 向上，逐層**拆信封**，叫解封裝（De-encapsulation）。

```
[  L7 Data：GET /index.html HTTP/1.1  ]
   ↓ L4 加上 TCP Header（來源/目的 Port）
[ TCP Header | HTTP Data ]
   ↓ L3 加上 IP Header（來源/目的 IP）
[ IP Header | TCP Header | HTTP Data ]
   ↓ L2 加上 Ethernet Header（來源/目的 MAC）+ FCS 檢查碼
[ Eth Header | IP Header | TCP Header | HTTP Data | FCS ]
   ↓ L1 轉成 0 與 1 電子訊號傳輸
01001000 01100101 01101100 01101100 01101111...
```

---

## 各設備處理的層級

| 設備 | 處理到哪層 | 說明 |
|------|-----------|------|
| **網路線 / Wi-Fi** | L1 | 只傳 0 與 1 |
| **交換器 (Switch)** | L2 | 看 MAC 位址，在 LAN 內轉發 |
| **路由器 (Router)** | L3 | 看 IP 位址，決定跨網路路徑 |
| **防火牆 (Firewall)** | L3-L4 | 過濾 IP 和 Port |
| **你的電腦** | L1-L7 | 完整封裝與解封裝 |

---

## 業界常用的層級溝通語言

> **筆記重點**
> 雖然網際網路實際運行的是 TCP/IP 模型，但工程師在跟同事或網管討論問題時，仍習慣用 OSI 的「層」來描述狀況。因為 OSI 分層更細，講「第幾層出問題」能更精準地指出故障範圍。

- **「這個問題出在 L3」** → IP 設定或路由器有問題
- **「檢查一下 L1」** → 去看網路線有沒有插好
- **「L7 負載平衡」** → 根據 HTTP 內容來分流

---

## 前端工程師聚焦的層（L5–L7）

> **筆記重點**
> 對前端工程師而言，最直接打交道的就是 L7 應用層——你寫的每一行 `fetch` 或 `axios` 請求，都是在這一層運作的。理解這層的運作方式，能幫助你掌握 API 呼叫、狀態碼與標頭等日常開發核心。

| 層 | 前端工程師日常接觸 |
|----|----------------|
| **L7** | `fetch()`, `axios`, HTTP methods, Status codes, REST API |
| **L6** | `JSON.stringify()` / `JSON.parse()`, HTTPS/TLS, charset, GZIP |
| **L5** | Cookie, Session, JWT, CORS |
| **L4** | TCP 連線數 → HTTP/2 多路復用 → WebSocket |
