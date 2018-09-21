import discord, logging, json
from discord.ext import commands
from profanity import profanity
from tinydb import TinyDB, Query
from tinydb.operations import delete,increment
import time
import random


# Requirements: discord.py, tinydb, profanity

# Define all variables to be used around the script
description = '''Bot description here'''
bot = commands.Bot(command_prefix='-', description=description)
db = TinyDB('data.json')
Users = Query()
TOKEN = ''
#TOKEN = ''
vc = 52

# Print the starting text
print('---------------')
print('Sample Bot')
print('---------------')
print('Starting Bot...')

# Setup basic logging for the bot
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print('Bot is ready for use')



@bot.command(pass_context=True)
async def join(context):
	path = './audio/audio_' + str(random.randint(1,31)) + '.ogg'
	await bot.send_message(context.message.channel,path)
	vc = await bot.join_voice_channel(context.message.author.voice_channel)
	player = vc.create_ffmpeg_player(path, after=lambda: print('done'))
	player.start()
	while(player.is_playing()):
		time.sleep(2)
	await vc.disconnect()

@bot.command(pass_context=True)
async def ptzrr(context):
	path = './audio/audio_14.ogg'
	await bot.send_message(context.message.channel,path)
	vc = await bot.join_voice_channel(context.message.author.voice_channel)
	player = vc.create_ffmpeg_player(path, after=lambda: print('done'))
	player.start()
	while(player.is_playing()):
		time.sleep(2)
	await vc.disconnect()

@bot.command(pass_context=True)
async def castillo(context):
	player = vc.create_ffmpeg_player('./audio_1.ogg', after=lambda: print('done'))
	player.start()

@bot.command(pass_context = True)
async def leave(ctx):
	return await vc.disconnect()


if __name__ == '__main__':
	bot.run(TOKEN)