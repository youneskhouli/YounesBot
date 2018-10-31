# https://discordapp.com/oauth2/authorize?client_id=503950766239776784&scope=bot&permissions=67648

import discord
import sys
import random
import asyncio

class YounesBot(discord.Client):
    token = open("token.txt", 'r').read()

    async def on_ready(self):
        print(f'We have logged in as {self.user} with ID: {self.user.id}')
        print('-------')

    async def on_message(self, message):  # event that happens per any message.
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        if "bot shutdown" in message.content.lower() and message.author.name == "Younes":
            await self.close()
            sys.exit()
        # do not to yourself, that would be weird. 
        if message.author.id == self.user.id:
            return

        if message.content.startswith('guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))

    def startbot(self):
        self.run(self.token)

bot = YounesBot()
bot.startbot()
