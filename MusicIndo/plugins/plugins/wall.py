import random

import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from MusicIndo import app


@app.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):

    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text("`Please give some query to search.`")
    m = await message.reply_text("sᴇᴀʀᴄʜɪɴɢ...")
    try:
        url = requests.get(f"https://api.safone.dev/wall?query={text}").json()[
            "results"
        ]
        ran = random.randint(0, 7)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ʟɪɴᴋ", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception as e:
        await m.edit_text(
            f"`ᴡᴀʟʟᴘᴀᴘᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ : `{text}`",
        )


__MODULE__ = "ᴡᴀʟʟ"
__HELP__ = """
<b>ᴄᴏᴍᴍᴀɴᴅꜱ:</b>
/WALL - ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴇɴᴅ ᴡᴀʟʟᴘᴀᴘᴇʀ.

<b>ɪɴꜰᴏ:</b>
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴇɴᴅ ᴡᴀʟʟᴘᴀᴘᴇʀ.
- ᴜsᴇ /WALL ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴀ ᴛᴇxᴛ ᴛᴏ ꜱᴇᴀʀᴄʜ ғᴏʀ ᴡᴀʟʟᴘᴀᴘᴇʀ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ.

<b>ɴᴏᴛᴇ:</b>
- ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴇɴᴅ ᴡᴀʟʟᴘᴀᴘᴇʀ.
"""
