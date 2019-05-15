import discord
improt os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("test")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("야"):
        await message.channel.send('뭐')

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
