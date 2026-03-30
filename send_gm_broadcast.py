import os, random, requests, sys

TOKEN = os.environ.get("LINE_ACCESS_TOKEN")
if not TOKEN:
    sys.exit("請先在環境變數或 Actions Secret 設定 LINE_ACCESS_TOKEN")

GITHUB_USERNAME = "ycchenn" 
REPO_NAME = "GoodMorning_linebot"
BRANCH_NAME = "main"

IMAGE_FILES = [
    "goodmorning01.png"
]

def broadcast_image(url: str):
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {"messages": [{"type":"image","originalContentUrl":url,"previewImageUrl":url}]}
    r = requests.post("https://api.line.me/v2/bot/message/broadcast",
                      headers=headers, json=payload, timeout=15)
    r.raise_for_status()
    print("Broadcast OK:", url)

if __name__ == "__main__":
    if not IMAGE_FILES:
        print("錯誤：IMAGE_FILES 清單是空的")
        sys.exit(1)
    
    selected_image_file = random.choice(IMAGE_FILES)
    
    target_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH_NAME}/images/{selected_image_file}"
    
    try:
        broadcast_image(target_url)
    except Exception as e:
        print(f"失敗了: {e}")
        sys.exit(1)