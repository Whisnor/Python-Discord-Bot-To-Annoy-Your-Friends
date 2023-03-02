import discord.client
from discord.ext import commands

TOKEN = "(bot token)"
bot = commands.Bot(command_prefix="£", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I will put annoy (friend's name) messages".format(bot))

id = "(friend'd discord id as an interger)"

@bot.event
async def on_message(message):
    if "(friend's name)]" and "good" in message.content:
        await message.add_reaction("\U0001F913")
    if "(friends name)" and "bad" in message.content:
        await message.add_reaction("\U0001F4AA")
    if message.author.id == id:
        await message.add_reaction("\U0001F913")
        user = bot.get_user(id)
        await user.send("(message for your friend)")
    else:
        print(f"{message.author}:\n{message.content}")

bot.run(TOKEN)
