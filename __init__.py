# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/grass"
__description__ = "Count how many grasses (laughes) a telegram user said"
__dname__ = "grass"

from telethon import events, utils
from telethon.extensions import markdown
def setup(bot,storage):
    grasses = ["☘️","🌱","🍀","🌿","草"]
    @bot.on(events.NewMessage())
    async def grass_msg(event):
        for x in grasses:
            if x in event.message.text:
                grass_times = storage.get("grass_" + str(event.sender.id),0)
                grass_times += 1
                if grass_times % 10 == 0:
                    await event.reply("恭喜，[{}](tg://user?id={})已經草了{}次！".format(utils.get_display_name(event.sender),event.sender.id,grass_times))
                storage.set("grass_" + str(event.sender.id), grass_times)
                break
    @bot.on(events.NewMessage(pattern='/grass'))
    async def grass(event):
        if event.is_private:
            grass_times = storage.get("grass_" + str(event.sender.id),0)
            await event.respond("您已經草了{}次！".format(grass_times))
        else:
            user = event.sender
            reply = await event.get_reply_message()
            if reply:
                user = await reply.get_sender()
            grass_times = storage.get("grass_" + str(user.id),0)
            await event.respond("[{}](tg://user?id={})已經草了{}次！".format(utils.get_display_name(user),user.id,grass_times))

