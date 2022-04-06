import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30868ddf51d5599e8c777.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
✨ ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ᴀɴᴅ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ...
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Simple_Mundaa) ...
━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("♦️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ♦️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("📝 ᴄᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"),
            InlineKeyboardButton("⚕️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Simple_Mundaa")
        ],
        [
            InlineKeyboardButton("📛 sᴜᴘᴘᴏʀᴛ", url="https://t.me/SECRET_SOCIETY012"),
            InlineKeyboardButton("🎑 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/DEMON_CREATORS")
        ],
        [
            InlineKeyboardButton("💠 ʏᴏᴜᴛᴜʙᴇ 💠", url="https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw")
        ]
    ]
)
    
    
@Client.on_message(commandpro(["/start", "/alive", "Sumit"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30868ddf51d5599e8c777.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/World_FriendShip_Zone")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["DarkxMusic","Sumit", "#Channel", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/65be304b45005b8bd84db.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇs", url=f"https://t.me/Demon_Creators")
                ]
            ]
        ),
    )
