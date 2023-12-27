import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TeamXBharat import LOGGER, app, userbot
from TeamXBharat.core.call import CHAMPU
from TeamXBharat.misc import sudo
from TeamXBharat.plugins import ALL_MODULES
from TeamXBharat.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ ᴠᴀʀɪᴀʙʟᴇs ɴᴏᴛ ᴅᴇғɪɴᴇᴅ, ᴇxɪᴛɪɴɢ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("TeamXBharat.plugins" + all_module)
    LOGGER("TeamXBharat.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await CHAMPU.start()
    try:
        await CHAMPU.stream_call("https://graph.org/file/37508c2235191fa104e3f.mp4")
    except NoActiveGroupCall:
        LOGGER("TeamXBharat").error(
            "ᴘʟᴇᴀsᴇ ᴛᴜʀɴ ᴏɴ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴏғ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ.\n\nsᴛᴏᴘᴘɪɴɢ ʙᴏᴛ..."
        )
        exit()
    except:
        pass
    await CHAMPU.decorators()
    LOGGER("TeamXBharat").info(
        "ᴍᴀᴅᴇ ʙʏ 𝗧ᴇᴧᴍ ꭙ 𝗕ʜᴧꝛᴧᴛ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("TeamXBharat").info("sᴛᴏᴘᴘɪɴɢ ᴄʜᴀᴍᴘᴜ's ᴍᴜsɪᴄ ʙᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())