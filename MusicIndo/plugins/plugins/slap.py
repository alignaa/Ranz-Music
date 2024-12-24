from MusicIndo import app
from pyrogram import filters
import nekos


@app.on_message(filters.command("slap"))
async def slap(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(
                nekos.img("slap"),
                caption=f"{message.from_user.mention} sʟᴀᴘᴘᴇᴅ {message.reply_to_message.from_user.mention}",
            )
        else:
            await message.reply_video(nekos.img("slap"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")


__MODULE__ = "ꜱʟᴀᴘ"
__HELP__ = """
ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:
- /sʟᴀᴘ: ꜱʟᴀᴘꜱ ꜱᴏᴍᴇᴏɴᴇ. ɪғ ᴜꜱᴇᴅ ᴀꜱ ᴀ ʀᴇᴘʟʏ, ꜱʟᴀᴘꜱ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴜꜱᴇʀ.
"""

