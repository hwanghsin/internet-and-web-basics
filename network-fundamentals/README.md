# 網路基礎知識（Network Fundamentals）

本區以**概念為主**，程式碼為輔助說明工具。每個主題包含：
- `README.md`：核心概念與圖表說明
- `demo.py`：Python 程式展示（可直接執行）
- `demo.html`：瀏覽器互動範例（帶有 OSI 層對應的 HTML 註解）

---

## 五階段學習路線

| 階段 | 主題 | 資料夾 |
|------|------|--------|
| **Stage 1** | 網路參考模型（OSI / TCP-IP） | [04-osi-model](./04-osi-model/) / [05-tcp-ip-model](./05-tcp-ip-model/) |
| **Stage 2** | 定址與身份（IP / MAC） | [01-ip-addressing](./01-ip-addressing/) |
| **Stage 3** | 通訊協定（DNS / DHCP / HTTP） | [02-request-response](./02-request-response/) / [03-client-server](./03-client-server/) |
| **Stage 4** | 硬體設備（Switch / Router） | [03-client-server](./03-client-server/) 中的 DNS/路由說明 |
| **Stage 5** | 實戰工具（Wireshark / DevTools） | 各資料夾的 demo.html 均有 DevTools 觀察提示 |

---

## 與 web-basics 的關係

```
network-fundamentals/             web-basics/
 └─ 02-request-response/    ←→    javascript/03-fetch-api/
      HTTP 理論                        fetch() 實作
```

`javascript/03-fetch-api/index.html` 是兩大主題的**橋接點**，
從 JS 的 `fetch()` 呼叫中可以看到 DNS 查詢、TCP 握手、HTTP request 的完整流程。

---

## 原始筆記主題對應

| 筆記主題 | 對應資料夾 |
|----------------------|-----------|
| 網路架構（ISP、IP、Request/Response） | `01-ip-addressing` / `02-request-response` |
| 使用者端（HTTP headers、status codes） | `02-request-response` |
| 效能（minify、file 數量、HTML 解析） | `02-request-response` |
| 網路型態（LAN/MAN/WAN、Protocols） | `01-ip-addressing` |
| 伺服器端（Port 80、index.html） | `03-client-server` |
