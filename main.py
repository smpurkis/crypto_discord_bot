import os
from pathlib import Path

from discord.ext import commands
from dotenv import load_dotenv

dot_env_file_exist = Path('.env').exists()
if dot_env_file_exist:
    load_dotenv()
TOKEN = str(os.getenv("DISCORD_BOT_TOKEN"))
print("Successfully loaded Discord token")

bot = commands.Bot(command_prefix="!")


@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)


@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')


@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)


bot.run(TOKEN)
