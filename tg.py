import os
import json
import youtube_dl
from telegram import Bot, InputMediaVideo

# Загрузка конфигурации
with open('channels.json') as f:
    channels = json.load(f)

# Функция для загрузки видео с YouTube
def download_video(video_url, output_path):
    ydl_opts = {
        'outtmpl': output_path,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Функция для загрузки видео в Telegram канал
def upload_video_to_telegram(video_path, channel_id, bot_token):
    bot = Bot(token=bot_token)
    bot.send_video(chat_id=channel_id, video=open(video_path, 'rb'))

# Перебор всех каналов
for channel in channels:
    channel_id = channel['telegram_channel_id']
    bot_token = channel['telegram_bot_token']
    video_url = channel['youtube_video_url']

    # Загрузка видео с YouTube
    output_path = 'video.mp4'
    download_video(video_url, output_path)

    # Загрузка видео в Telegram канал
    upload_video_to_telegram(output_path, channel_id, bot_token)

    # Удаление видео с компьютера
    os.remove(output_path)

print("Видео успешно загружены и удалены.")
