# GoodMorning Line Bot (Broadcast, GitHub Actions)

每天早上 08:00（台北時間） 自動透過 LINE Messaging API 廣播一張「早安圖」給所有把此 bot 加為好友的人。
本專案採用 GitHub Actions 定時執行，無需自架伺服器。

---

## 特色

1.無伺服器：用 GitHub Actions 觸發排程

2.極簡程式：一支 Python 腳本

3.安全：Token 使用 Actions Secrets 保存

4.可客製：可同時送文字、調整排程時間、替換圖片清單

---

## 運作流程

GitHub Actions 在指定時間觸發 →

安裝依賴 →

以環境變數 LINE_ACCESS_TOKEN（從 Secrets 來）執行 send_gm_broadcast.py →

透過 LINE API 對所有好友廣播圖片。

---

## 先決條件

一個 LINE Developers → Messaging API Channel

取得 Channel access token (long-lived)

讓收訊者把你的 bot 加為好友（被封鎖就收不到）

GitHub repo（Right here）

---


## 常見問題

401/403：Token 錯誤或權限不足，請確認使用的是 Messaging API 的長效 Token。

400：圖片連結不是公開 HTTPS、Content-Type 不正確，或圖片過大。

收不到：對方沒加好友、或把 bot 封鎖。

額度：官方免費方案每月約 500 則訊息；超過需升級方案。

測試成功但排程沒跑：確認 Actions 未被停用、gm.yml 在 .github/workflows/、分支設定正確、cron 時區為 UTC。