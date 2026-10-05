# GRW Feedback Server

Flask server that receives base64 screenshots and forwards them to Telegram.

## Endpoints

- `GET /` — health check
- `POST /` — upload image

### POST body (form-urlencoded)

- `base64_image` — URL-encoded base64 image (required)
- `caption` — caption text (optional)

## Environment Variables

- `BOT_TOKEN` — Telegram bot token
- `CHAT_ID` — Telegram chat ID

## Deploy

1. Push to GitHub
2. Connect repo to Render
3. Set `BOT_TOKEN` and `CHAT_ID` in Environment
4. Deploy
