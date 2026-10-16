#!/usr/bin/env python3
"""
NORTH7 Webhook Agent — Polls every 5 min, sends alerts on high-score signals.

pip install north7 requests
export NORTH7_API_KEY=your_key
export TELEGRAM_BOT_TOKEN=your_bot_token
export TELEGRAM_CHAT_ID=your_chat_id
python webhook_agent.py
"""
import os, time, requests
from north7 import North7Client
from datetime import datetime, timezone

POLL_INTERVAL = 300  # 5 minutes
MIN_SCORE = 75       # only alert on high-confidence signals
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "")

def send_alert(msg):
    """Send via Telegram. Replace with Slack/Discord/email as needed."""
    if TELEGRAM_TOKEN and TELEGRAM_CHAT:
        requests.post("https://api.telegram.org/bot%s/sendMessage" % TELEGRAM_TOKEN,
                       data={"chat_id": TELEGRAM_CHAT, "text": msg, "parse_mode": "HTML"})
    print(msg)

def run():
    client = North7Client()
    seen = set()

    print("NORTH7 Webhook Agent started. Polling every %ds, min score %d." % (POLL_INTERVAL, MIN_SCORE))

    while True:
        try:
            risk = client.risk()
            signals = client.signals()

            for s in signals:
                ticker = getattr(s, 'ticker', None) or getattr(s, 'symbol', '?')
                score = getattr(s, 'risk_score', 0) or 0
                action = getattr(s, 'action', getattr(s, 'direction', '?'))
                key = "%s_%s_%s" % (ticker, action, datetime.now(timezone.utc).strftime("%Y-%m-%d"))

                if score >= MIN_SCORE and key not in seen:
                    seen.add(key)
                    msg = (
                        "<b>NORTH7 ALERT</b>\n"
                        "%s <b>%s</b> (score %d)\n"
                        "Risk Index: %s (%s)"
                    ) % (action, ticker, score, risk.risk_index, risk.label)
                    send_alert(msg)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print("Error: %s" % str(e)[:60])

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    run()
