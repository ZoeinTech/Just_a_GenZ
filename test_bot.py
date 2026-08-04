from unittest.mock import MagicMock, patch
from main import fetch_news

def test_broken_feed():
    fake_feed = MagicMock()
    fake_feed.entries = []

    with patch('feedparser.parse', return_value=fake_feed):
       result = fetch_news(['http://broken-feed-example.com/rss'], limit=3)
       assert "Just a GenZ Digest" in result
       assert "Here are the latest news articles" in result