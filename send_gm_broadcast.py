import os, random, requests, sys

TOKEN = os.environ.get("LINE_ACCESS_TOKEN")
if not TOKEN:
    sys.exit("請先在環境變數或 Actions Secret 設定 LINE_ACCESS_TOKEN")

IMAGES = []

def broadcast_image(url: str):
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {"messages": [{"type":"image","originalContentUrl":url,"previewImageUrl":url}]}
    r = requests.post("https://api.line.me/v2/bot/message/broadcast",
                      headers=headers, json=payload, timeout=15)
    r.raise_for_status()
    print("Broadcast OK:", url)