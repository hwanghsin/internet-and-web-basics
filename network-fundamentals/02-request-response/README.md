# HTTP 請求與回應（Request & Response）

## 基本概念

網頁與伺服器的互動只有兩種：**Request（請求）** 與 **Response（回應）**。

> **筆記重點**
> 網頁與伺服器之間的所有溝通，本質上只有兩個動作：瀏覽器送出「請求（Request）」，伺服器回以「回應（Response）」。再複雜的網站行為，拆解到底層都是由這一來一往所組成。

---

## HTTP 請求結構

當使用者從網頁發出一個請求時，必須帶有 **Request Headers**：

| Header | 說明 | 範例 |
|--------|------|------|
| **Method** | 操作類型（RESTful） | `GET` / `POST` / `PUT` / `DELETE` |
| **Path** | 網域後的路徑 | `/content` / `/api/users/123` |
| **Host** | 目標伺服器的網域 | `google.com` / `github.com` |
| **Cookie** | 附加的使用者資訊 | `session_id=abc123` |
| **Content-Type** | 請求 body 的格式（POST/PUT 時） | `application/json` |

### HTTP Methods（RESTful 語義）

| Method | 用途 | 有 Body？ |
|--------|------|----------|
| `GET` | 取得資源 | 否 |
| `POST` | 新增資源 | 是 |
| `PUT` | 更新資源（整體替換） | 是 |
| `DELETE` | 刪除資源 | 否 |

---

## HTTP 回應結構

伺服器回傳的 **Response** 一定包含：

| 項目 | 說明 | 範例 |
|------|------|------|
| **Status Code** | 回傳狀態 | `200 OK` |
| **Content-Type** | 回傳內容格式 | `text/html` / `application/json` |
| **Body** | 實際內容 | HTML、JSON、圖片資料 |

### Status Codes 總覽

| 範圍 | 意義 | 常見狀態碼 |
|------|------|-----------|
| **2xx** | 成功 | `200 OK`、`201 Created`、`204 No Content` |
| **3xx** | 重定向 | `301 Moved Permanently`、`304 Not Modified` |
| **4xx** | 客戶端錯誤 | `400 Bad Request`、`401 Unauthorized`、`404 Not Found` |
| **5xx** | 伺服器錯誤 | `500 Internal Server Error`、`502 Bad Gateway` |

---

## 效能：為什麼要 Minify？

> **筆記重點**
> 一份 HTML 引用的 CSS 與 JS 檔案數量越少，整體載入效能就越好——因為每多引用一個檔案，瀏覽器就得多發一次 HTTP 請求，請求次數少自然能更快完成存取。此外，許多 CSS 與 JS 會經過「minify（壓縮）」處理：把檔案裡的空格、換行等多餘字元刪除，藉此縮小檔案體積、加快傳輸。

- **請求次數越少，載入越快**：每個 `<link>` 或 `<script>` 都是一個 HTTP 請求
- **Minify**：刪除空格、換行、縮短變數名，減少檔案大小，傳輸更快
- **典型命名**：`main.min.css`、`jquery.min.js`

---

## HTTP 版本演進

| 版本 | 傳輸層 | 關鍵改進 |
|------|--------|---------|
| **HTTP/1.1** | TCP | 同一網域同時最多 6 個連線，有隊頭阻塞 |
| **HTTP/2** | TCP | 多路復用（Multiplexing）、Header 壓縮（HPACK）、Server Push |
| **HTTP/3** | UDP（QUIC） | 0-RTT 握手、連線遷移、更徹底的分流 |

### 前端工程師的意義

- 以前需要合併 50 個圖示成一張大圖（CSS Sprite）→ 因為 HTTP/1.1 連線數限制
- HTTP/2 後，發送多個小請求不再是效能毒藥
- HTTP/3 讓 Wi-Fi 切換 4G 時連線不斷

---

## HTML 解析流程

> **筆記重點**
> 伺服器把網頁回傳後，瀏覽器會從 HTML 文件的最上方逐行往下解析，先處理 `<head>` 再進入 `<body>`。過程中一旦遇到引用的外部檔案（CSS、JS、圖片），就會另外發出請求把它們抓回來，最後才將完整內容渲染在畫面上。

```
1. 瀏覽器發出 GET / HTTP/1.1
2. 伺服器回傳 HTML 文件
3. 瀏覽器從 <head> 開始逐行解析
4. 遇到 <link> → 發出 HTTP 請求取 CSS
5. 遇到 <script> → 發出 HTTP 請求取 JS（會阻塞解析！）
6. 解析 <body> 並渲染畫面
```

---

## 前端快速診斷公式

| 問題現象 | 對應 OSI 層 | 診斷方向 |
|---------|-----------|---------|
| 報錯 4xx/5xx | L7（HTTP） | 看 Request/Response headers 是否正確 |
| API 拿不到資料（CORS） | L5（Session/Security） | Browser 跨域安全規範 |
| 網頁白屏很久 | L4（Transport） | DNS 太慢？TCP 請求太多？ |
| 亂碼問題 | L6（Presentation） | Encoding 設定（charset=UTF-8？） |
