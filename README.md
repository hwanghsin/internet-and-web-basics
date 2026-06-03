# internet-and-web-basics

網路跟網頁基礎知識筆記

---

## 目錄結構

```
├── network-fundamentals/       # 網路基礎（概念導向，Demo 為輔）
│   ├── 01-ip-addressing/       # IP 位址、IPv4/IPv6、DHCP、NAT
│   ├── 02-request-response/    # HTTP Request/Response、Status Codes、Minify
│   ├── 03-client-server/       # DNS、Port、Client-Server 架構
│   ├── 04-osi-model/           # OSI 七層模型、封裝/解封裝
│   └── 05-tcp-ip-model/        # TCP vs UDP、三向握手、HTTP/2/3
│
└── web-basics/                 # 網頁基礎（程式碼導向，瀏覽器直接執行）
    ├── html/
    │   ├── 01-structure/       # DOCTYPE、meta、路徑、實體字元、Canvas、SVG
    │   ├── 02-forms/           # Input types、驗證、表單屬性
    │   └── 03-semantic/        # 語意標籤、媒體元素、表格
    ├── css/
    │   ├── 01-box-model/       # 盒模型、display、置中、CSS 變數/函式
    │   ├── 02-flexbox/         # Flex 容器/項目屬性、互動沙盒
    │   └── 03-grid/            # Grid 欄列、跨欄跨列、常見版型
    └── javascript/
        ├── 01-dom-manipulation/ # 查詢、新增/修改/刪除節點、classList
        ├── 02-event-handling/   # 冒泡/捕獲、委派、自訂事件
        ├── 03-fetch-api/        # ← 橋接點：網路概念 ↔ JS 實作
        └── 04-async-await/      # Callback → Promise → async/await
```

## 橋接點

`javascript/03-fetch-api/` 把網路基礎和 JS 實作連結起來——
每次 `fetch()` 呼叫都走完 DNS → TCP → TLS → HTTP 的完整流程。
