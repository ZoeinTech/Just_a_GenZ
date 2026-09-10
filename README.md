# Just_a_GenZ

A Telegram bot that fetches the latest articles from a list of RSS feeds, formats them into a digest, and sends them to Telegram automatically on a schedule via GitHub Actions.

## Features

- **RSS Parsing**: Pulls the latest articles from multiple RSS feeds using `feedparser`.
- **Digest Formatting**: Formats titles, links, publish dates, and summaries into a single readable digest.
- **Telegram Delivery**: Sends the digest directly to a Telegram chat via the Telegram Bot API.
- **Automated Schedule**: Runs automatically on a weekly schedule using GitHub Actions (no server required).
- **Manual Trigger**: Can also be triggered manually for testing or on-demand digest generation.

## Built With

- **Python 3**
- **feedparser** — RSS parsing
- **requests** — HTTP calls to the Telegram API
- **python-dotenv** — Local environment variable management
- **GitHub Actions** — Scheduled automation
- **Telegram Bot API**

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Telegram bot

1. Message `@BotFather` on Telegram.
2. Use `/newbot` and follow the prompts to get your bot token.
3. Send your new bot a message, then visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` to find your `chat_id`.

### 4. Set up environment variables

Create a `.env` file in the project root (this file is git-ignored and never committed):

```env
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

## Usage

Run the script manually to test:

```bash
python main.py
```

If your `.env` is set up correctly, you should see a success message printed, and the digest will arrive in your Telegram chat.

## Automation (GitHub Actions)

This project runs automatically every Wednesday at 9:00 AM UTC via a GitHub Actions workflow (`.github/workflows/`).

To enable it on your own fork:

1. Go to your repo's **Settings** → **Secrets and variables** → **Actions**.
2. Add two repository secrets: `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`.
3. The workflow will run automatically on schedule, or can be triggered manually from the **Actions** tab using **Run workflow**.

## Configuration

RSS feed sources are set in `main.py`:

```python
urls = [
    "https://www.vox.com/rss/culture/index.xml",
    "https://pudding.cool/rss.xml"
]
```

Add or remove feed URLs here to change what the digest pulls from. The `limit` parameter controls how many articles are pulled per feed.

## Testing

Unit tests are written with `pytest` and cover the article-formatting logic (including handling of broken/empty feeds) without making real network calls:

```bash
pytest test_bot.py -v
```

## Contributing

<!-- TODO: Add contribution guidelines -->

## License

<!-- TODO: Add license details -->
