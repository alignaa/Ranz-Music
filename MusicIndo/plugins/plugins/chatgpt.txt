from pyrogram import filters
from pyrogram.enums import ChatAction
from TheApi import api

from MusicIndo import app
from config import BANNED_USERS


@app.on_message(filters.command(["chatgpt", "ai", "ask"]) & ~BANNED_USERS)
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/ai write simple website code using html css, js?`"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    results = api.chatgpt(user_input)
    await message.reply_text(results)


__MODULE__ = "ᴄʜᴀᴛɢᴘᴛ"
__HELP__ = """
<blockquote>
➢ <b>ᴄʜᴀᴛɢᴘᴛ ᴄᴏᴍᴍᴀɴᴅꜱ</b>

`/advice` - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
`/ai [ǫᴜᴇʀʏ]` - ᴀꜱᴋ ʏᴏᴜʀ ǫᴜᴇꜱᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ'ꜱ ᴀɪ
`/gemini [ǫᴜᴇʀʏ] - ᴀꜱᴋ ʏᴏᴜʀ ǫᴜᴇꜱᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ'ꜱ ɢᴇᴍɪɴɪ ᴀɪ
`/bard [ǫᴜᴇʀʏ]` - ᴀꜱᴋ ʏᴏᴜʀ ǫᴜᴇꜱᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ'ꜱ ʙᴀʀᴅ ᴀɪ
</blockquote>
"""
