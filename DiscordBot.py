# https://discordapp.com/oauth2/authorize?client_id=503950766239776784&scope=bot&permissions=67648

import discord
import sys
import random

class YounesBot(discord.Client):
    words = ['Dude', 'Mate', 'Friend', 'body', 'Man']
    token = open("token.txt", 'r').read()

    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):  # event that happens per any message.
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        if message.author != self.user and message.author.name == "evilcanofsoda":
            await message.channel.send(f"What do you want {random.choice(self.words)}")
        if "bot shutdown" in message.content.lower() and message.author.name == "Younes":
            await self.close()
            sys.exit()

    def startbot(self):
        self.run(self.token)

bot = YounesBot()
bot.startbot()
