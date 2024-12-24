from MusicIndo import app
from pyrogram import filters
import nekos


@app.on_message(filters.command("hug"))
async def huggg(client, message):
    try:
        if message.reply_to_message:
            await message.reply_video(
                nekos.img("hug"),
                caption=f"{message.from_user.mention} hugged {message.reply_to_message.from_user.mention}",
            )
        else:
            await message.reply_video(nekos.img("hug"))
    except Exception as e:
        await message.reply_text(f"Error: {e}")


__MODULE__ = "ʜᴜɢ"
__HELP__ = """
ᴛʜɪꜱ ʙᴏᴛ ʀᴇꜱᴘᴏɴᴅꜱ ᴛᴏ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴍᴍᴀɴᴅꜱ:
- /hug: ꜱᴇɴᴅꜱ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ.

<b>ᴄᴏᴍᴍᴀɴᴅꜱ</b>
- /hug: ꜱᴇɴᴅꜱ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ. ɪғ ᴜꜱᴇᴅ ᴀꜱ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴍᴇꜱꜱᴀɢᴇ, ɪᴛ ᴍᴇɴᴛɪᴏɴꜱ ᴛʜᴇ ꜱᴇɴᴅᴇʀ ᴀɴᴅ ʀᴇᴄɪᴘɪᴇɴᴛ ᴏғ ᴛʜᴇ ʜᴜɢ.

<b>ʜᴏᴡ ᴛᴏ ᴜꜱ</b>
- ᴜꜱᴇ /hug ᴛᴏ ꜱᴇɴᴅ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ.
- Rʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴡɪᴛʜ /hu ᴛᴏ ꜱᴇɴᴅ ᴀ ʜᴜɢɢɪɴɢ ᴀɴɪᴍᴀᴛɪᴏɴ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴛʜᴇ ꜱᴇɴᴅᴇʀ ᴀɴᴅ ʀᴇᴄɪᴘɪᴇɴᴛ.

<b>ɴᴏᴛᴇꜱ</b>
- ᴇɴꜱᴜʀᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ꜱᴇᴛᴛɪɴɢꜱ ᴀʟʟᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ꜱᴇɴᴅ ᴠɪᴅᴇᴏꜱ/ꜱᴛɪᴄᴋᴇʀꜱ ᴀꜱ ʀᴇᴘʟɪᴇꜱ ғᴏʀ ғᴜʟʟ ғᴜɴᴄᴛɪᴏɴᴀʟɪᴛʏ."""
