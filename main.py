import time
import requests
import json
import base64

TOKEN = "느그들 토큰넣어라"

properties_dict = {
    "os": "Windows",
    "browser": "Chrome",
    "device": "",
    "system_locale": "ko-KR",
    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "browser_version": "115.0.0.0",
    "os_version": "10",
    "referrer": "",
    "referring_domain": "",
    "release_channel": "stable",
    "client_build_number": 27201,
    "client_event_source": None
}

PROPERTIES = base64.b64encode(json.dumps(properties_dict).encode()).decode()

URL = "https://discord.com/api/v9/users/@me/clan"

HEADERS = {
    "accept": "*/*",
    "accept-language": "en-US,ko-KR;q=0.9",
    "authorization": TOKEN,
    "content-type": "application/json",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "ko",
    "x-discord-timezone": "Asia/Seoul",
    "x-super-properties": PROPERTIES
}

guild_ids = [
    "1369817361040932974",
    "1373591846940442708",
    "1300099843125018705"
]

while True:
    for guild_id in guild_ids:
        payload = {
            "identity_guild_id": guild_id,
            "identity_enabled": True
        }
        response = requests.put(URL, headers=HEADERS, data=json.dumps(payload))
        time.sleep(0.1)
