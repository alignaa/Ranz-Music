from pyrogram import filters
from MusicIndo import app
from TheApi import api


@app.on_message(filters.command("hastag"))
async def hastag(bot, message):

    try:
        text = message.text.split(" ", 1)[1]
        res = api.gen_hashtag(text)
    except IndexError:
        return await message.reply_text("Example:\n\n/hastag python")

    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ :\n<pre>{res}</pre>", quote=True)


__MODULE__ = "ʜᴀꜱʜᴛᴀɢ"
__HELP__ = """
<b>ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ:</b>

• `/hashtag [text]`: ɢᴇɴᴇʀᴀᴛᴇ ʜᴀꜱʜᴛᴀɢꜱ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
