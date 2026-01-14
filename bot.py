import requests
import time
import hashlib

# ===== YOUR INFO =====
BOT_TOKEN = "8455266168:AAG5MpcL307-KRnCITrXgHGrH04IO6cuizs"
CHAT_ID = "6754145366"

CHECK_INTERVAL = 15  # seconds (FAST)

INTENT_WORDS = [
    "need help",
    "looking for help",
    "need someone",
    "looking for someone",
    "hire someone",
    "pay someone",
    "anyone available"
]

JOB_WORDS = [
    "yard",
    "lawn",
    "cleaning",
    "moving",
    "haul",
    "junk",
    "handyman",
    "repair",
    "paint",
    "assembly",
    "installation",
    "side job",
    "cash",
    "today",
    "asap"
]

SEARCH_URL = "https://nextdoor.com/search/posts/?q={}"
seen = set()

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

def check():
    for intent in INTENT_WORDS:
        url = SEARCH_URL.format(intent.replace(" ", "+"))
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            continue

        text = r.text.lower()
        for job in JOB_WORDS:
            if intent in text and job in text:
                key = hashlib.md5((intent + job).encode()).hexdigest()
                if key not in seen:
                    seen.add(key)
                    send(
                        f"🚨 NEW SIDE JOB FOUND\n\n"
                        f"Intent: {intent}\n"
                        f"Job: {job}\n\n"
                        f"🔗 Check Nextdoor now:\n{url}"
                    )

send("✅ Side-job alert bot is LIVE")

while True:
    try:
        check()
        time.sleep(CHECK_INTERVAL)
    except:
        time.sleep(10)
