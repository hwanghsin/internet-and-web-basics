# TCP/IP 模型與傳輸協定

## TCP vs UDP

| 特性 | TCP | UDP |
|------|-----|-----|
| **可靠性** | 保證送到（掛號信） | 不保證（平信） |
| **速度** | 較慢（需確認） | 較快（發了就算） |
| **順序** | 保證順序 | 不保證順序 |
| **連線** | 需要握手 | 無連線 |
| **用途** | HTTP, HTTPS, 電子郵件 | 影片串流, DNS, UDP/QUIC |

---

## TCP 三向握手（Three-way Handshake）

在 HTTP 請求發出之前，Client 和 Server 必須先建立 TCP 連線：

```
Client                     Server
  |── SYN（我想連，序號 X）──→|
  |←── SYN-ACK（好，序號 Y）──|
  |── ACK（收到了）──────────→|
  |                           |
  |──── HTTP GET 請求 ─────→ |
  |←─── HTTP Response ──────|
```

> **筆記重點**
> 三向握手可以用一段對話來理解：
> - **SYN**：你的電腦先開口——「嗨 Google，我有事想跟你說，你方便嗎？」
> - **SYN-ACK**：Google 回應——「收到了，我也準備好跟你對話了。」
> - **ACK**：你的電腦確認——「太好了，那我們開始傳資料吧！」
>
> 三個步驟走完，雙方才正式建立起可靠的連線。

---

## OSI 七層 vs TCP/IP 四層

| OSI 七層（理論標準） | TCP/IP 四層（實際應用） | 重點協定 |
|---------------------|----------------------|---------|
| L7 應用層 | **應用層 (Application)** | HTTP, DNS, SMTP |
| L6 展示層 | ↑ 同上 | SSL/TLS, UTF-8 |
| L5 會話層 | ↑ 同上 | Session, Cookie |
| L4 傳輸層 | **傳輸層 (Transport)** | TCP, UDP |
| L3 網路層 | **網路層 (Internet)** | IP, ICMP |
| L2 資料連結層 | **網路存取層 (Network Access)** | Ethernet, MAC |
| L1 實體層 | ↑ 同上 | 網路線, Wi-Fi |

> **筆記重點**
> 可以把兩者想成「藍圖」與「成屋」的關係：OSI 七層模型是詳盡的「建築藍圖」，把每一層的職責都規範得清清楚楚；TCP/IP 四層模型則是實際蓋好的「成屋」——因為現實中有些層級往往會綁在一起處理，於是就把它們合併成更精簡的結構。

---

## HTTP 版本與傳輸層的關係

| 版本 | L4 傳輸層 | 關鍵特性 |
|------|----------|---------|
| HTTP/1.1 | TCP | 隊頭阻塞（Head-of-Line Blocking）；同域最多 6 個 TCP 連線 |
| HTTP/2 | TCP | 多路復用（Multiplexing）；所有請求共用同一個 TCP 連線 |
| HTTP/3 | UDP（QUIC） | 0-RTT 握手；連線遷移；獨立流（掉包只影響單一流） |

### 為什麼需要 HTTP/3？

HTTP/2 雖然解決了「應用層的隊頭阻塞」，但 TCP 本身有個弱點：
若某個 TCP 封包丟失，整個連線都要等待重傳。
HTTP/3 用 **QUIC（基於 UDP）** 取代 TCP，讓不同資料流互相獨立，掉包只影響那個流。

### 連線遷移（Connection Migration）

- HTTP/1.1 / HTTP/2：換 Wi-Fi → IP 改變 → TCP 斷線 → 重新握手
- HTTP/3：靠 Connection ID 識別，換網路不斷線

---

## WebSocket

WebSocket 是建立在 TCP（L4）之上的**全雙工**通訊協定：

```
HTTP 握手升級：
GET /chat HTTP/1.1
Upgrade: websocket
Connection: Upgrade

→ 之後 Client 和 Server 可以雙向即時傳訊，不需每次都重新建立連線
```

用途：即時聊天室、即時通知、協作工具（如 Google Docs）

---

## 前端效能診斷

```
網頁載入很慢時：
├── DNS Lookup 很久？     → CDN / dns-prefetch（L7 DNS）
├── Initial Connection？  → 伺服器離使用者太遠（L4 TCP 握手）
├── SSL 很久？            → HTTP/3 的 0-RTT（L6 TLS）
├── TTFB 很久？           → 後端 API / 資料庫太慢（L7 應用層）
└── Content Download？    → 圖片未壓縮 / JS 未打包（傳輸量）
```
