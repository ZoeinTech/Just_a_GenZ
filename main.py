import requests
import os
from dotenv import dotenv_values
from pathlib import Path
import feedparser
import schedule
from datetime import datetime
import time


def fetch_news(urls,limit=3):
    digest = "Just a GenZ Digest\n\n"
    digest += "Here are the latest news articles:\n\n"
    digest += "-" * 50 + "\n"


    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            title = entry.get("title", "No title available")
            link = entry.get("link", "No link available")
            summary = entry.get("summary", "No summary available")
            date = entry.get("published", "No date available")
            digest += f"Title: {title}\n"
            digest += f"Read more here: {link}\n"
            digest += f"Date: {date}\n"
            digest += f"Summary: {summary}\n"
            digest += "-" * 50 + "\n"

    return digest

def send_message_to_telegram(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # print masked url for debugging (do not log the real token in production)

    payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, json=payload)
    print(response.status_code, response.text)


    




def main():
    urls = ["https://www.vox.com/rss/culture/index.xml",
            "https://pudding.cool/rss.xml"]
    articles = fetch_news(urls, limit=3)
    print(articles)
    send_message_to_telegram(articles)
        


if __name__ == "__main__":
    print("Local run testing...")
    main()
   


