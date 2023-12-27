import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","itsMeShivanshu")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "TheChampuBot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "TheChampuBot")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "TheChampu")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "6969"))


# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", ))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6399386263))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TheChampu/MusicXBharat",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Champu")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TheChampuStore")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Chatting_Club01")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/198796f3ccc75371ab627.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/198796f3ccc75371ab627.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d0afbc0637f8fa3a95587.jpg"
STATS_IMG_URL = "https://telegra.ph/file/c97eab3ee44c7fef1d7e4.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/198796f3ccc75371ab627.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/eca8a684f8ca5d6634c7a.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/994ec4ecbe07c89fa398c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d0afbc0637f8fa3a95587.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/fb9181859efb3c6a514d2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d0afbc0637f8fa3a95587.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/d0afbc0637f8fa3a95587.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d0afbc0637f8fa3a95587.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
