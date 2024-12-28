from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from config import MUST_JOIN
from pyrogram import filters

async def subscribed(client, update):
    user_id = update.from_user.id
    if user_id in MUST_JOIN:
        return True

    try:
        member = await client.get_chat_member(chat_id=MUST_JOIN, user_id=user_id)
        return member.status in [
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.MEMBER
        ]
    except UserNotParticipant:
        return False

is_subscriber = filters.create(subscribed)